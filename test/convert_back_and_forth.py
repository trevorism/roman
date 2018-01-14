import unittest

from src.convert_to_arabic import ConvertToArabic
from src.convert_to_roman import ConvertToRoman


class ConvertAllTests(unittest.TestCase):
    arabic_converter = ConvertToArabic()
    roman_converter = ConvertToRoman()

    def testAll(self):
        for x in range(0, 3000):
            roman = self.roman_converter.convert(x)
            arabic = self.arabic_converter.convert(roman)
            print(roman)
            self.assertEqual(x, arabic)


if __name__ == "__main__":
    unittest.main()
