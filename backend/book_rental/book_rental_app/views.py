import requests
from datetime import datetime
from dateutil import relativedelta, parser
from django.db.models import Count
import pytz
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Student, Rental, Book
from .serializers import StudentSerializer, BookSerializer, RentalSerializer, RentalFetchSeializer


class StudentView(APIView):
  def get(self, request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({ "message": "students fetched successfully", "data": serializer.data})
  
  def post(self, request):
    serializer = StudentSerializer(data=request.data)
  
    if serializer.is_valid():
      serializer.save()
    else:
      return Response(serializer.errors, status=400)
    
    return Response({ "message": "student created successfully", "data": serializer.data})
  
class SingleStudentView(APIView):
  def get(self, request, pk):
    try: 
      student = Student.objects.get(id=pk)
      print(student)
      serializer = StudentSerializer(student, many=False)
      return Response({ "message": "student fetched successfully", "data": serializer.data})
    except Student.DoesNotExist: 
      return Response({ "message": "student not found"}, status=404)
  
  def put(self, request, pk):
    student = Student.objects.get(id=pk)
    print(request.data)
    serializer = StudentSerializer(instance= student, data=request.data)
    if serializer.is_valid():
      serializer.save()
    
    return Response({ "message": "students updated successfully", "data": serializer.data})

class BookView(APIView):
  def get(self, request):
    q = request.GET.get('q', '')
    limit = request.GET.get('limit', 10)
    offset = request.GET.get('offset', 0)
    url = "https://openlibrary.org/search.json"
    params = { 'title': q, "fields": "title,number_of_pages,number_of_pages_median,key,cover_edition_key", "limit": limit, "offset": offset}
    r = requests.get(url = url, params = params)
    data = r.json()
    return Response({ "message": "books query successfully", "data": data })



class RentalView(APIView):
  def get(self, request):
    rental = Rental.objects.all()
    serializer = RentalFetchSeializer(rental, many=True)
    return Response({ "message": "rentals fetched successfully", "data": serializer.data})
  
  def post(self, request):
    data = request.data
    edition_key = data['edition_key']
    # check if book exists in db
    book = Book.objects.filter(edition_key=edition_key).first()
    book_id = book.id if book is not None else ''
    if book is None:
      try:

        url = f"https://openlibrary.org/book/{edition_key}.json"
        r = requests.get(url = url)
        r_data = r.json()
        print(r_data)
        book_data = {
          "edition_key": edition_key,
          "book_title": r_data['title'],
          "number_of_pages": r_data['number_of_pages'] if r_data['number_of_pages'] else r_data['number_of_pages_median']
        }
        serializer = BookSerializer(data=book_data)
    
        if serializer.is_valid():
          serializer.save()
          book = serializer.data
          book_id = book['id']
        else: 
          return Response({ "message": "failed to create rental. Please select some other bookt"}, status=400)
          
      except Exception as e:
        return Response({ "message": "failed to create rental. Please select some other book"}, status=400)
    return_date = parser.parse(data['return_date'])
    if return_date < datetime.now():
      return Response({ "message": "Invalid rental date" }, status=400)
    delta = relativedelta.relativedelta(return_date, datetime.now())
    month_diff = (delta.years * 12) + delta.months
    rental_charge = month_diff * book.number_of_pages / 100 if month_diff > 1 else 0
    # Save rental
    rental_data = {
      "student": data['student_id'],
      "book": book_id,
      "rented_at": datetime.now(),
      "return_date": return_date,
      "rental_charge": rental_charge
    }
    print(rental_data)
    rental_serializer = RentalSerializer(data=rental_data)
    print(rental_serializer)
    if rental_serializer.is_valid():
      print("rental serializer is valid")
      rental_serializer.save()
    else:
      return Response(rental_serializer.errors, status=400)
    
    return Response({ "message": "rental created successfully", "data": rental_serializer.data})
  
class SingleRentalView(APIView):
  def get(self, request, pk):
    try: 
      rental = Rental.objects.get(id=pk)
      print(rental.book.book_title)
      serializer = RentalFetchSeializer(rental, many=False)
      return Response({ "message": "rental fetched successfully", "data": serializer.data})
    except Rental.DoesNotExist: 
      return Response({ "message": "rental not found"}, status=404)
    
  def patch(self, request, pk):
    data = request.data
    return_date = pytz.UTC.localize(parser.parse(data['return_date']))
    rental = Rental.objects.get(id=pk)
    # validate new rental date
    if return_date < rental.rented_at:
      return Response({ "message": "Invalid rental date" }, status=400)
    # calculate new charge
    delta = relativedelta.relativedelta(return_date, rental.rented_at)
    month_diff = (delta.years * 12) + delta.months
    rental_charge = month_diff * rental.book.number_of_pages / 100 if month_diff > 1 else 0
    serializer = RentalSerializer(rental, data = {'rental_charge': rental_charge, 'return_date': return_date }, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({ "message": "rental updated successfully", "data": serializer.data})
    else: 
      return Response(serializer.errors, status=500 )
    
class AnalyticsView(APIView):
  def get(self, request):
    number_of_rentals = Rental.objects.count()
    number_of_student = Student.objects.count()
    active_student = Student.objects.annotate(number_of_rentals=Count("rental")).order_by("-number_of_rentals")
    most_active_student = active_student[0] if len(active_student) > 0 else None
    rented_book = Book.objects.annotate(number_of_rentals=Count("rental")).order_by("-number_of_rentals")
    most_rented_book = rented_book[0] if len(rented_book) > 0 else None
    response_data = {
      "number_of_rentals": number_of_rentals,
      "number_of_student": number_of_student,
      # "most_active_student": StudentSerializer(most_active_student, many =False).data,
      "most_active_student": f'{most_active_student.first_name} {most_active_student.last_name} ({most_active_student.number_of_rentals})' if most_active_student else '',
      # "most_rented_book": BookSerializer(most_rented_book, many =False).data
      "most_rented_book": f'{most_rented_book.book_title} ({most_rented_book.number_of_rentals})' if most_rented_book else ''
    }
    print(response_data)
    return Response({'message': 'Analytics data fetched successfully', "data": response_data})