"""Flask server for the Watson NLP emotion detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the application interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Return emotion scores for the text supplied by the user."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
