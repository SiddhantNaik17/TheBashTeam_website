import dialogflow_v2 as dialogflow

PROJECT_ID = 'custom-watch-296215'
SESSION_ID = '123456789'


class DialogFlow:
    def __init__(self):
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(PROJECT_ID, SESSION_ID)

    def detect_intent_texts(self, text):
        text_input = dialogflow.types.TextInput(text=text, language_code='en')
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        return response
