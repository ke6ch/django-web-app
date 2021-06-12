import json
from django.conf import settings
from ibm_watson import ApiException
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class Watson(object):
    API_KEY = getattr(settings, "API_KEY", None)
    URL = getattr(settings, "URL", None)
    VERSION = getattr(settings, "VERSION", None)
    ASSISTANT_ID = getattr(settings, "ASSISTANT_ID", None)

    def __init__(self):
        authenticator = IAMAuthenticator(self.API_KEY)
        self.assistant = AssistantV2(version=self.VERSION, authenticator=authenticator)
        self.assistant.set_service_url(self.URL)

        try:
            response = self.assistant.create_session(
                assistant_id=self.ASSISTANT_ID
            ).get_result()

            self.session_id = response["session_id"]
        except ApiException as ex:
            if ex.code == "404":
                print(ex.message)
                raise Exception
            else:
                raise Exception

    def send_message(self, message):
        try:
            response = self.assistant.message(
                assistant_id=self.ASSISTANT_ID,
                session_id=self.session_id,
                input={"message_type": "text", "text": message},
            ).get_result()

            return response

        except ApiException as ex:
            if ex.code == 404:
                print(ex.message)
                raise Exception
        except Exception:
            raise Exception

    def __del__(self):
        try:
            response = self.assistant.delete_session(
                assistant_id=self.ASSISTANT_ID, session_id=self.session_id
            ).get_result()
            print(json.dumps(response, indent=2))

        except ApiException as ex:
            if ex.code == "404":
                print(ex.message)
                raise Exception
            else:
                raise Exception


if __name__ == "__main__":
    watson = Watson()
    watson.send_message("あそぼー")
