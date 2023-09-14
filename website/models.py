from base.models import BaseModel
from django.db import models


class Record(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")


