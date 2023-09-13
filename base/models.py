from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField("Created At", auto_now_add=True,)
    updated_at = models.DateTimeField("Updated_At", auto_now=True)
    
    class Meta:
        abstract=True