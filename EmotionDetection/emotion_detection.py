"""Emotion detection using the IBM Watson NLP emotion service."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_result():
    """Return the standard result for invalid input/API 400."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze):
    """Detect five emotions and determine the dominant emotion."""
    if text_to_analyze is None or not text_to_analyze.strip():
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        WATSON_URL,
        headers=WATSON_HEADERS,
        json=payload,
        timeout=15,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]

    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    result["dominant_emotion"] = max(emotions, key=emotions.get)
    return result
