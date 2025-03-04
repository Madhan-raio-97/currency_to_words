# Currency to Words (Indian System)

This is a Python package to convert numeric currency amounts into words, following the American, Indian numbering system.

## Installation

You can install the package using pip:

```bash
pip install currency_to_words


from currency_to_words import value

amount = 1234567.89
print(value(amount))  # Output: One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven Dollars And Eighty Nine Cents
```


### Full Implementation with All Cases:

Here is how you can implement the handling of these additional cases:


1. **Sentence case**:
   - This format capitalizes only the first letter of the first word of the sentence and makes all the other letters lowercase.
   - Example: `"One crore ninety two lakh three thousand four hundred seventy eight rupees and ninety paise"`

   **Logic**: `result[0].upper() + result[1:].lower()`

2. **Alternating case**:
   - This format alternates the case of each letter. The first letter is uppercase, the second is lowercase, the third is uppercase, and so on.
   - Example: `"OnE cRoRe nInEtY tWo lAkH tHrEe tHoUsAnD fOuR hUnDrEd sEvEnTy EiGhT rUpEeS aNd nInEtY pAiSe"`

   **Logic**: `''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(result)])`

3. **Upper Camel Case (Pascal Case)**:
   - This format capitalizes the first letter of each word and removes spaces.
   - Example: `"OneCroreNinetyTwoLakhThreeThousandFourHundredSeventyEightRupeesAndNinetyPaise"`

   **Logic**: `''.join([word.capitalize() for word in result.split()])`

4. **Lower Camel Case**:
   - This format is similar to Upper Camel Case, but the first word starts with a lowercase letter, while the subsequent words start with uppercase letters.
   - Example: `"oneCroreNinetyTwoLakhThreeThousandFourHundredSeventyEightRupeesAndNinetyPaise"`

   **Logic**: `words[0].lower() + ''.join([word.capitalize() for word in words[1:]])`

### Example Outputs:
1. **Uppercase**: `"ONE CRORE NINETY TWO LAKH THREE THOUSAND FOUR HUNDRED SEVENTY EIGHT RUPEES AND NINETY PAISE"`
2. **Lowercase**: `"one crore ninety two lakh three thousand four hundred seventy eight rupees and ninety paise"`
3. **Title Case**: `"One Crore Ninety Two Lakh Three Thousand Four Hundred Seventy Eight Rupees And Ninety Paise"`
4. **Capitalize**: `"One crore ninety two lakh three thousand four hundred seventy eight rupees and ninety paise"`
5. **Sentence Case**: `"One crore ninety two lakh three thousand four hundred seventy eight rupees and ninety paise"`
6. **Alternating Case**: `"OnE cRoRe nInEtY tWo lAkH tHrEe tHoUsAnD fOuR hUnDrEd sEvEnTy EiGhT rUpEeS aNd nInEtY pAiSe"`
7. **Upper Camel Case**: `"One Crore Ninety Two Lakh Three Thousand Four Hundred Seventy Eight Rupees And Ninety Paise"`
8. **Lower Camel Case**: `"one Crore Ninety Two Lakh Three Thousand Four Hundred Seventy Eight Rupees And Ninety Paise"`

Now the function can handle all the specified case formats. Just pass the desired case type as a parameter (`case_type='uppercase'`, `case_type='lowercase'`, etc.).
