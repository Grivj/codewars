"""
    Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

    Examples
        "the-stealth-warrior" gets converted to "theStealthWarrior"
        "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text):
    res = ''

    to_uppercase = False
    for i in range(len(text)):

        if is_underscore_or_dash(text[i]):
            to_uppercase = True

        elif to_uppercase:
            res += text[i].upper()
            to_uppercase = False
        else:
            res += text[i]

    return res


def is_underscore_or_dash(letter: str) -> bool:
    return letter in {'_', '-'}
