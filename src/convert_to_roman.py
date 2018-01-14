class ConvertToRoman:
    conversionMap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                     90: 'XC', 50: 'L', 10: 'X', 5: 'V', 4: 'IV', 1: 'I'}

    def convert(self, num):
        roman_string = ''
        for key in reversed(sorted(self.conversionMap)):
            while key <= num:
                roman_string = roman_string + self.conversionMap[key]
                num = num - key

        return roman_string
