import unittest
from mean_consume import MeanConsume


class TestMeanConsume(unittest.TestCase):
    def setUp(self):
        self.mean_consume = MeanConsume()

    def test_calculate_mean_consume(self):
        self.assertEqual(self.mean_consume.calculate_mean(
            1000, 2000, 150), "6.67")


if __name__ == '__main__':
    unittest.main()
