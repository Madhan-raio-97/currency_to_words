from utils.case import apply_case_transformation

from american_eng import number_to_currency_in_words
from indian_eng import convert_currency_to_words

result = ''

def value(amount, lang='EN', case_type='title'):

    if lang == 'EN':
        result = number_to_currency_in_words(amount)
    elif lang == 'INR':
        result = convert_currency_to_words(amount)
    

    return apply_case_transformation(result, case_type)