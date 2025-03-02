def apply_case_transformation(text, case_type='title'):
    """Apply the specified case transformation to the input text."""
    if case_type == 'uppercase':
        return text.upper()
    elif case_type == 'lowercase':
        return text.lower()
    elif case_type == 'title':
        return text.title()
    elif case_type == 'capitalize':
        return text.capitalize()
    elif case_type == 'sentence':
        return text[0].upper() + text[1:].lower()
    elif case_type == 'alternating':
        return ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)])
    elif case_type == 'upper_camel':
        return ' '.join([word.capitalize() for word in text.split()])
    elif case_type == 'lower_camel':
        words = text.split()
        return words[0].lower() + ''.join([word.capitalize() for word in words[1:]])

    # Default to 'title' case if no case_type is matched
    return text.title()
