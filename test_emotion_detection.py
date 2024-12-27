import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], "joy")

        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["dominant_emotion"], "anger")

        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response["dominant_emotion"], "disgust")

        response = emotion_detector("I am so sad about this")
        self.assertEqual(response["dominant_emotion"], "sadness")

        response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response["dominant_emotion"], "fear")

unittest.main()