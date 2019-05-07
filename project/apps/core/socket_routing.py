from django.urls import re_path

from core.consumers import AppointmentConsumer

websocket_urlpatterns = [
    re_path(r'^ws/appointments/$', AppointmentConsumer),
]
