from google.cloud import dialogflow
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../home/th3f1x/Documentos/iris-prby-43f07cc09b63.json"

def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={'session': session, 'query_input': query_input}
        )

        print('Query text:', response.query_result.query_text)
        print('Detected intent:', response.query_result.intent.display_name)
        print('Detected intent confidence:', response.query_result.intent_detection_confidence)
        print('Fulfillment text:', response.query_result.fulfillment_text)


def process_intent(intent_name, parameters):
    # Implemente lógica para cada intenção
    if intent_name == 'Saudacao':
        return 'Olá! Como posso ajudar?'

    elif intent_name == 'ObterInformacoes':
        # Use os parâmetros para realizar ação específica
        resposta = obter_informacoes(parameters['entidade'])
        return resposta

    else:
        return 'Desculpe, não entendi.'

def obter_informacoes(entidade):
    # Implemente lógica para obter informações com PyTorch
    # ...

    return 'Aqui estão as informações sobre ' + entidade

