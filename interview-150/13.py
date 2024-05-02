def romanToInt(s: str) -> int:
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    pointer = 0

    while pointer < len(s):
        if pointer < len(s) - 1 and roman_numbers[s[pointer]] < roman_numbers[s[pointer+1]]:
            total += roman_numbers[s[pointer+1]] - roman_numbers[s[pointer]]
            pointer += 2
        else:
            total += roman_numbers[s[pointer]]
            pointer += 1
    return total