import unittest
import math
from lesson_09.homework_09_2 import Sphere, calculate_volume

class TestSphere(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("begin")

    @classmethod
    def tearDownClass(cls):
        print("end")

    def test_sphere_positive_values(self):
        test_cases = [
            (1, 4/3 * math.pi * 1**3),
            (2.2, 4/3 * math.pi * 2.2**3),
            (0.5, 4/3 * math.pi * 0.5**3),
            (9, 4 / 3 * math.pi * 9**3)
        ]
        for radius, expected_volume in test_cases:
            with self.subTest(radius=radius):
                sphere = Sphere(radius=radius)
                actual_volume = calculate_volume(sphere)
                self.assertAlmostEqual(actual_volume, expected_volume, places=3)

    def test_sphere_negative_values_for_valueError(self):
        for radius in [-1, 0, -10]:
            with self.subTest(radius=radius):
                with self.assertRaises(ValueError) as context:
                    Sphere(radius=radius)
                # self.assertEqual(str(context.exception), "Radius must be positive")
                self.assertIn("positive", str(context.exception))

    def test_sphere_negative_values_for_TypeError(self):
        for radius in ['a', ' ', '$']:
            with self.subTest(radius=radius):
                with self.assertRaises(TypeError) as context:
                    Sphere(radius=radius)
                self.assertIn("number", str(context.exception))

if __name__ == "__main__":
    unittest.main()