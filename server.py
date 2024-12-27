from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    dominant_emotion = response["dominant_emotion"]
    response.pop("dominant_emotion")

    formatted_emotions = str(response).replace("{", "").replace("}", "")

    return "For the given statement, the system response is {}. The dominant emotion is <b>{}</b>".format(formatted_emotions, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)