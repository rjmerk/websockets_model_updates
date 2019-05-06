from django.conf import settings
from django.db import models


class Appointment(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    appointment_date = models.DateField()
    description = models.TextField(
        default='')
    last_modified = models.DateTimeField(
        auto_now=True)
