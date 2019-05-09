from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
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

    def save(self, *args, **kwargs):
        super().save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            settings.MAIN_CHANNEL,
            {
                "type": "appointment_update",
                "appointment_date": self.appointment_date.isoformat(),
                "user_id": self.user_id,
                "description": self.description
            }
        )
