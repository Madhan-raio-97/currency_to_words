def convert_number_to_words(n):
    if n == 0:
        return "zero"
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", 
            "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def convert_hundreds(num):
        if num == 0:
            return ""
        elif num < 20:
            return ones[num]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
        else:
            return ones[num // 100] + " hundred" + ('' if num % 100 == 0 else ' ' + convert_hundreds(num % 100))

    def convert(num):
        if num == 0:
            return "zero"
        result = ""
        part_count = 0
        while num > 0:
            if num % 1000 != 0:
                result = convert_hundreds(num % 1000) + ('' if thousands[part_count] == "" else ' ' + thousands[part_count]) + (" " + result if result else "")
            num //= 1000
            part_count += 1
        return result.strip()

    return convert(n)

def number_to_currency_in_words(amount):
    # Split the amount into dollars and cents
    dollars = int(amount)
    cents = round((amount - dollars) * 100)
    
    # Convert the dollar part to words
    dollar_words = convert_number_to_words(dollars) + " dollar" + ("s" if dollars != 1 else "")
    
    # If there are cents, convert the cent part to words
    if cents > 0:
        cent_words = convert_number_to_words(cents) + " cent" + ("s" if cents != 1 else "")
        return f"{dollar_words} and {cent_words}"
    else:
        return dollar_words
