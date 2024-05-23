from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=254)
    phone_number = models.PhoneNumberField(unique=True)

class Candidate(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit: #*1024*1024
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    image = models.ImageField(upload_to="/images", validators=[validate_image])
    name = models.CharField(max_length=191)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Education(models.Model):
    institute = models.CharField(max_length=191)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=191)
    country = models.CharField(max_length=191)
    degree = models.CharField(max_length=191)
    CATEGORY_CHOICES = (
    ("BACHELORS", "BACHELORS"),
    ("MASTERS", "MASTERS"),
    )
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default="BACHELORS")


