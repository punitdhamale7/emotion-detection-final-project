# Emotion Detection using IBM Watson NLP

A Flask web application that sends text to the IBM Skills Network Watson NLP emotion service and returns scores for anger, disgust, fear, joy, and sadness, plus the dominant emotion.

## Project name
Emotion Detection Application

## Run

```bash
python -m pip install -r requirements.txt
python server.py
```

Open `http://127.0.0.1:5000/` in a browser.

## Unit tests

```bash
python test_emotion_detection.py
```

The unit tests mock the HTTP response intentionally. This makes the tests repeatable while the application itself uses the real Watson endpoint.

## Static analysis

```bash
pylint server.py
pylint EmotionDetection/emotion_detection.py
```

## GitHub

After creating your public repository, put its URL here before submitting Question 1.
