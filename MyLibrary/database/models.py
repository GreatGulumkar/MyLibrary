from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=32)


class BookProfile(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    publication = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    available = models.PositiveIntegerField(default=0)


class BorrowRecord(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    book = models.ForeignKey("BookProfile", on_delete=models.CASCADE)
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    due_date = models.DateField()
