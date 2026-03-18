"""
This module hosts a Flask application that analyzes text for emotional content.
It uses the EmotionDetection package built over Watson NLP library to detect 
the dominant emotion and its associated sentiment scores.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main index HTML page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Retrieves the text to analyze from the query parameters, 
    passes it to the emotion_detector function, and formats the output.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    response = emotion_detector(text_to_analyze)
    # Check if a dominant emotion was successfully identified
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    # Formatting output string
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )
    return formatted_response

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
