import unittest
import requests

class TestClosest(unittest.TestCase):
    def test_home_is_helpful(self):
        res = requests.get('http://127.0.0.1:5000')
        self.assertIn("This will describe the API", str(res.content))

    def test_naked_closest_doesnt_fail(self):
        res = requests.get('http://127.0.0.1:5000/closest_sale')
        self.assertIn("No coordinates", str(res.content))

if __name__=="__main__":
    unittest.main()

