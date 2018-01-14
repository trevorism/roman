import unittest

from src.convert_to_arabic import ConvertToArabic


class ConvertToArabicTest(unittest.TestCase):
    convert_to_arabic = ConvertToArabic()

    def test_100(self):
        self.assertEqual(100, self.convert_to_arabic.convert('C'))

    def test_272(self):
        self.assertEqual(272, self.convert_to_arabic.convert('CCLXXII'))

    def test_996(self):
        self.assertEqual(996, self.convert_to_arabic.convert('CMXCVI'))

    def test_1904(self):
        self.assertEqual(1904, self.convert_to_arabic.convert('MCMIV'))


if __name__ == "__main__":
    unittest.main()