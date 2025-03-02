# utils/methods.py
from utils.assets import units, tens

def convert_two_digits(n):
    """Convert a number less than 100 to words"""
    if n == 0:
        return ""
    elif n < 20:
        return units[n]  # units should have words for 0-19
    else:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + units[n % 10])  # tens should have words for 10, 20, ..., 90


def convert_three_digits(n):
    """Convert a number less than 1000 to words"""
    if n == 0:
        return ""
    elif n < 100:
        return convert_two_digits(n)
    else:
        return units[n // 100] + " Hundred" + ('' if n % 100 == 0 else ' ' + convert_two_digits(n % 100))
