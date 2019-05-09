from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings
import json


class AppointmentConsumer(WebsocketConsumer):

    def connect(self):
        user = self.scope["user"]
        if user.is_authenticated or True:
            self.accept()
            async_to_sync(self.channel_layer.group_add)(
                settings.MAIN_CHANNEL,
                self.channel_name)
        else:
            self.close()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            settings.MAIN_CHANNEL,
            self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.send(text_data=json.dumps({
            "message": "Welcome! you said {}".format(message)
        }))

    def appointment_update(self, event):
        if(event["user_id"] != self.scope["user"].pk):
            return

        self.send(text_data=json.dumps({
            "appointment_date": event["appointment_date"],
            "description": event["description"]
        }))
