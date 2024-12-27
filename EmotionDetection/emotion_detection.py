import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = data, headers = header)

    if (response.status_code == 400):
        return dict.fromkeys(["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"], None)

    emotion_predictions = response.json()["emotionPredictions"]
    emotions = {}
    dominant_emotion = ('', 0.0)
    for prediction in emotion_predictions:
        for emotion, score in prediction["emotion"].items():
            if score > dominant_emotion[1]:
                dominant_emotion = (emotion, score)
            emotions[emotion] = score

    emotions["dominant_emotion"] = dominant_emotion[0]
    return emotions