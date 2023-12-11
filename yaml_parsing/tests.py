import unittest
from yaml_parsing.detect import detect_app_type


class TestAppDetection(unittest.TestCase):
    def app(self, name):
        return detect_app_type(f"example_apps/{name}-hello-world")

    def test_normal(self):
        self.assertEqual(self.app("c"), "c")
        self.assertEqual(self.app("java"), "java")
        self.assertEqual(self.app("javascript"), "javascript")
        self.assertEqual(self.app("python"), "python")
        self.assertEqual(self.app("befunge"), "befunge")

    def test_wrong(self):
        self.assertRaises(ValueError, detect_app_type, ".") # Wrong type of folder
        self.assertRaises(ValueError, detect_app_type, "faziufhiuazhf") # No such folder

