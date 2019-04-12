from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class VoteResultConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'events',
            self.channel_name
        )
        self.close()

    def events_alarm(self, event):
        self.send_json(
            {
                'type': 'events.alarm',
                'content': event['content']
            }
        )
