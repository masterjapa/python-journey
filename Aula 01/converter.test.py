import unittest
from converter import Converter


class TestConvertFunction(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()

    def test_convert_to_real(self):
        self.assertEqual(self.converter.convert_donation(1), 5.51)


if __name__ == '__main__':
    unittest.main()
