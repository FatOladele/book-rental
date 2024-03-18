import uuid
from datetime import date
from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Student(TimeStampedModel, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  student_id = models.CharField(unique=True, max_length=50)

class Book(TimeStampedModel, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  edition_key = models.CharField(max_length=50, unique=True)
  book_title = models.CharField(max_length=50)
  number_of_pages = models.IntegerField()

class Rental(TimeStampedModel, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  rented_at = models.DateTimeField(default= timezone.now)
  return_date = models.DateTimeField()
  rental_charge = models.FloatField(default=0)