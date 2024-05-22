from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class UserDevices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    DeviceName = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=100)
    Model = models.CharField(max_length=200)
    Watt = models.IntegerField()

    def __str__(self):
        return self.DeviceName+"\n"+self.manufacturer+"\n"+self.Model+"\n"+self.Watt
