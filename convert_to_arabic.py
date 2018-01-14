class ConvertToArabic:
    conversion_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def convert(self, roman):
        arabic = 0
        x=0
        while x < len(roman):
            if x != len(roman)-1 and self.conversion_map[roman[x]] < self.conversion_map[roman[x+1]]:
                arabic = arabic + self.conversion_map[roman[x+1]] - self.conversion_map[roman[x]]
                x = x + 1
            else:
                arabic = arabic + self.conversion_map[roman[x]]
            x = x + 1
        return arabic
