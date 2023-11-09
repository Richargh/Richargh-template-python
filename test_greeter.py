import unittest
from greeter import Greeter


class GreeterTest(unittest.TestCase):
    def test_can_greet_given_name(self):
        name = "Alex"
        app = Greeter(name)
        self.assertEqual(app.speak(), name)
