# Emotion Detection Application

A Flask web application that sends text to the IBM Skills Network Watson NLP emotion service and returns scores for anger, disgust, fear, joy, and sadness, plus the dominant emotion.

## Project Name
Emotion Detection Application

## Course Project Details
- **Project Title:** Final Project: AI-Based Web Application Development and Deployment
- **Application Name:** Emotion Detection Application
- **Repository URL:** https://github.com/punitdhamale7/emotion-detection-final-project
- **Author:** Punit Dhamale (punitdhamale7)

## Run

`ash
python -m pip install -r requirements.txt
python server.py
`

Open http://localhost:5000/ in a browser.

## Unit tests

`ash
python test_emotion_detection.py
`

## Static analysis

`ash
pylint server.py
pylint EmotionDetection/emotion_detection.py
`
