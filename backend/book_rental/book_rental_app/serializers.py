from rest_framework import serializers
from .models import Student, Book, Rental

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
  # student = StudentSerializer()
  # book_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
  # student = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
  # book = BookSerializer(many=False, read_only=True, source=)
  # book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all() ,many=False, read_only=True)
  class Meta:
    model = Rental
    fields = '__all__'

class RentalFetchSeializer(serializers.ModelSerializer):
  student = StudentSerializer(many=False, read_only=True)
  book = BookSerializer(many=False, read_only=True)
  class Meta:
    model = Rental
    fields = '__all__'