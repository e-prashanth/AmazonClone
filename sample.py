def isValidRoman(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    total = 0
    consecutive_count = 0

    for numeral in reversed(roman):
        value = roman_numerals.get(numeral)
        if value is None:
            return False  # Invalid Roman numeral

        if value == prev_value:
            consecutive_count += 1
            if consecutive_count > 3:
                return False  # Invalid Roman numeral
        else:
            consecutive_count = 1

        if value < prev_value:
            if prev_value / value not in [5, 10]:
                return False  # Invalid Roman numeral
            total -= value
        else:
            if prev_value > 0 and prev_value / value not in [1, 5]:
                return False  # Invalid Roman numeral
            total += value
        prev_value = value

    return True, total

def main():
    roman_input = input("Enter a Roman number: ")
    isValid = isValidRoman(roman_input)
    if isinstance(isValid, bool):
        if isValid:
            print("Valid Roman number")
        else:
            print("Invalid Roman number")
    else:
        print("Valid Roman number. Decimal equivalent:", isValid[1])

if __name__ == "__main__":
    main()
