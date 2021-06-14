import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .watson import Watson


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.watson = Watson()

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        del self.watson

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    async def chat_message(self, event):
        try:
            response = self.watson.send_message(event["message"])
            generics = response["output"]["generic"]

            text = ""
            for generic in generics:
                text = generic["text"]

            await self.send(text_data=json.dumps({"message": text}))

        except Exception as e:
            await self.send(text_data=json.dumps({"message": e.__class__.__name__}))
            del self.watson
