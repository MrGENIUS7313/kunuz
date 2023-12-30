from django.db import models
import uuid


class BaseModels(models.Model):
    #yaratilganini kuni va soati bilan bir xil qilib olish uchun yana bittasini qoshish kerak 
    create_day = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract=True