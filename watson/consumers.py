import json

from channels.generic.websocket import WebsocketConsumer

from .watson import Watson


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.watson = Watson()

    def disconnect(self, close_code):
        del self.watson

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]

            response = self.watson.send_message(message)
            generics = response["output"]["generic"]

            text = ""
            for generic in generics:
                text = generic["text"]

            self.send(text_data=json.dumps({"message": text}))
        except Exception as e:
            print("error")
            print(e)
            del self.watson
