"""Server to receive text and return the detected emotions"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """Route for user to call the emotion detector function"""
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "<b>Invalid text! Please try again!</b>"

    response.pop("dominant_emotion")

    formatted_emotions = str(response).replace("{", "").replace("}", "")
    result = "For the given statement, the system response is " + formatted_emotions
    result += ". The dominant emotion is <b>" + dominant_emotion + "</b>"

    return result

@app.route("/")
def render_index_page():
    """Route to display the index page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
