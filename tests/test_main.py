import unittest
from main import estimated_steps


class BisectTests(unittest.TestCase):
    def test_estimated_steps(self):
        self.assertEqual(estimated_steps(1), 1)
        self.assertEqual(estimated_steps(7), 3)
        self.assertEqual(estimated_steps(8), 4)

    def test_invalid_distance(self):
        with self.assertRaises(ValueError):
            estimated_steps(0)


if __name__ == "__main__":
    unittest.main()
