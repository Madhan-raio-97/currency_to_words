# currency_to_words/__init__.py

from utils.methods import convert_two_digits, convert_three_digits

def convert_currency_to_words(amount, case_type='title'):
    """Convert a numeric amount to words (Indian numbering system) with case handling"""

    def num_to_words(n):
        """Convert a number to words for Indian currency system"""
        if n == 0:
            return "Zero"

        crore = n // 10000000
        n %= 10000000

        lakh = n // 100000
        n %= 100000

        thousand = n // 1000
        n %= 1000

        hundred = n

        words = []
        if crore > 0:
            words.append(convert_three_digits(crore) + " Crore")  # Use convert_three_digits for crore
        if lakh > 0:
            words.append(convert_three_digits(lakh) + " Lakh")  # Use convert_three_digits for lakh
        if thousand > 0:
            words.append(convert_three_digits(thousand) + " Thousand")  # Use convert_three_digits for thousand
        if hundred > 0:
            words.append(convert_three_digits(hundred))  # Use convert_three_digits for hundreds

        return ' '.join(words).strip()

    rupees = int(amount)
    paise = round((amount - rupees) * 100)

    rupees_in_words = num_to_words(rupees)

    if paise > 0:
        paise_in_words = num_to_words(paise)
        result = f"{rupees_in_words} Rupees and {paise_in_words} Paise"
    else:
        result = f"{rupees_in_words} Rupees"

    # Apply the case transformation based on the case_type parameter
    if case_type == 'uppercase':
        result = result.upper()
    elif case_type == 'lowercase':
        result = result.lower()
    elif case_type == 'title':
        result = result.title()
    elif case_type == 'capitalize':
        result = result.capitalize()
    elif case_type == 'sentence':
        result = result[0].upper() + result[1:].lower()
    elif case_type == 'alternating':
        result = ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(result)])
    elif case_type == 'upper_camel':
        result = ' '.join([word.capitalize() for word in result.split()])
    elif case_type == 'lower_camel':
        words = result.split()
        result = words[0].lower() + ' '.join([word.capitalize() for word in words[1:]])

    return result

# Test with an example
print(convert_currency_to_words(19992345678.90))  # Test with a larger value