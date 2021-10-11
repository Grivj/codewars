"""
    Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

    The keypad has the following layout:

    ┌───┬───┬───┐
    │ 1 │ 2 │ 3 │
    ├───┼───┼───┤
    │ 4 │ 5 │ 6 │
    ├───┼───┼───┤
    │ 7 │ 8 │ 9 │
    └───┼───┼───┘
        │ 0 │
        └───┘
    He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

    He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

    * possible in sense of: the observed PIN itself and all variations considering the adjacent digits

    Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

    Detective, we are counting on you!
"""
from itertools import product


def get_pins(observed):
    keypad = Keypad()
    adjacent_digits = []

    for digit in observed:
        x, y = keypad.get_digit_index(digit)
        adjacent_digits.append(keypad.get_adjacent_digits(x, y))
    return ["".join(p) for p in product(*adjacent_digits)]


class Keypad:
    def __init__(self, keypad: list = None):
        self.keypad = keypad or [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            [' ', '0', ' ']
        ]

    def get_digit_index(self, digit: str):
        for row_idx, row in enumerate(self.keypad):
            if digit in row:
                return row_idx, row.index(digit)

        raise IndexError(f"Digit '{digit}' not on the keypad.")

    def get_adjacent_digits(self, x: int, y: int):
        """
        Returns a list of digits adjacent to (x, y)
        from: 
            top digit (x - 1, y)
            middle digits (x, y - 1:y + 1)
            bottom digit (x + 1, y)
        """
        top = self.keypad[x - 1][y] if x != 0 else None
        mid = self.keypad[x][max(y - 1, 0): min(y + 2, 3)]
        bot = self.keypad[x + 1][y] if x < 3 else None

        if ' ' in mid:
            mid = [i for i in mid if i != ' ']

        digits = []
        if top:
            digits.append(top)
        for i in mid:
            digits.append(i)
        if bot and bot != ' ':
            digits.append(bot)
        return digits
