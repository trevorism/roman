import unittest

from convert_to_roman import ConvertToRoman


class ConvertToRomanTests(unittest.TestCase):
    converter = ConvertToRoman()

    def test_convert_100(self):
        self.assertEqual('C', self.converter.convert(100))

    def test_convert_323(self):
        self.assertEqual('CCCXXIII', self.converter.convert(323))

    def test_convert_494(self):
        self.assertEqual('CDXCIV', self.converter.convert(494))

    def test_convert_1904(self):
        self.assertEqual('MCMIV', self.converter.convert(1904))

