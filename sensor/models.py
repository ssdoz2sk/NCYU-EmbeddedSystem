import uuid

from django.db import models
from device.models import Device

# Create your models here.

class Sensor(models.Model):
    sensor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id = models.ForeignKey(Device)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
