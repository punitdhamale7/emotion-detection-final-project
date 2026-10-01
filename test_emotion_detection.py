"""Unit tests for the emotion detector.

The tests mock the Watson response so they are deterministic and do not
consume the external service during unit testing.
"""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestDominantEmotions(unittest.TestCase):
    """Verify dominant-emotion detection for all required emotions."""

    def _mock_response(self, dominant):
        scores = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
        }
        scores[dominant] = 0.90
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        return response

    def _get_dominant(self, text, dominant):
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=self._mock_response(dominant),
        ):
            return emotion_detector(text)["dominant_emotion"]

    def test_joy(self):
        self.assertEqual(self._get_dominant("I am glad this happened", "joy"), "joy")

    def test_anger(self):
        self.assertEqual(self._get_dominant("I am really mad about this", "anger"), "anger")

    def test_disgust(self):
        self.assertEqual(
            self._get_dominant("I feel disgusted about this", "disgust"), "disgust"
        )

    def test_sadness(self):
        self.assertEqual(self._get_dominant("I am very sad", "sadness"), "sadness")

    def test_fear(self):
        self.assertEqual(self._get_dominant("I am afraid", "fear"), "fear")


if __name__ == "__main__":
    unittest.main()
