"""
Test module for EmotionDetection package
"""

import unittest
from EmotionDetection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detection(self):
        """Test emotion detection with sample text"""
        result = emotion_detector("I love this new technology.")
        self.assertIsNotNone(result)
        self.assertIn('joy', result)
        
    def test_negative_text(self):
        """Test emotion detection with negative text"""
        result = emotion_detector("I hate working long hours.")
        self.assertIsNotNone(result)
        # Check if anger is the dominant emotion
        if result:
            dominant = max(result, key=result.get)
            self.assertEqual(dominant, 'anger')

if __name__ == '__main__':
    unittest.main()