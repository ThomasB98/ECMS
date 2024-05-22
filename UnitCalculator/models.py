from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import JSONField
from Authentication.models import UserDevices
import uuid
# Create your models here.


class SudoBillModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dynamic_data = JSONField()
    totalAmount = models.IntegerField()
    Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Sudo Bill by {self.Date} Total HoursRun {self.totalAmount} {self.id}"
