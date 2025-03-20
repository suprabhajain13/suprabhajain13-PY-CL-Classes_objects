# lab_test.py

import unittest
from src.main.lab import Lightbulb

class TestLightbulb(unittest.TestCase):
    def test_initial_state(self):
        # Test if the lightbulb is initially off
        bulb_off = Lightbulb(False)
        self.assertFalse(bulb_off.get_state())

        # Test if the lightbulb is initially on
        bulb_on = Lightbulb(True)
        self.assertTrue(bulb_on.get_state())
        
    def test_method_name(self):
        method_name = "get_description"
        class_methods = dir(Lightbulb)
        self.assertIn(method_name, class_methods, f"Method '{method_name}' not found in Lightbulb class.")
        self.assertTrue(callable(getattr(Lightbulb, method_name)), f"Method '{method_name}' is not callable.")


    def test_get_description(self):
        # Test description when the lightbulb is off
        bulb_off = Lightbulb(False)
        self.assertEqual(bulb_off.get_description(), "The bulb is off")

        # Test description when the lightbulb is on
        bulb_on = Lightbulb(True)
        self.assertEqual(bulb_on.get_description(), "The bulb is on")

    def test_set_state(self):
        # Test setting the lightbulb state to on
        bulb = Lightbulb(False)
        bulb.set_state(True)
        self.assertTrue(bulb.get_state())

        # Test setting the lightbulb state to off
        bulb.set_state(False)
        self.assertFalse(bulb.get_state())

if __name__ == '__main__':
    unittest.main()
