'''
We can assume that the input string contains tokens separated by a single whitespace.

Credit card numbers are represented by strings that contain anywhere from 13-16 digits (inclusive).
The function will analyze the input string and look for any token that looks
like a credit card (ie it contains between 13-16 digits).
The function will then replace all of the digits with an "x" character
EXCEPT for the last 4 digits for that token.
It will then return the full string with the data redacted.
Examples
// 16 digit number gets redacted, other tokens will not be touched
redact_card_numbers("1234567890123456 is a number")
returns "xxxxxxxxxxxx3456 is a number"
// No credit card found, no transformation needed
redact_card_numbers("basic_string 12345 no redaction")
returns "basic_string 12345 no redaction"
// 16 digit number in the middle of the string is redacted, other tokens are left alone.
redact_card_numbers("an embedded number 1234567890123456 in the string")
returns "an embedded number xxxxxxxxxxxx3456 in the string"

Cards issued by Visa will start with a 4 and will only have 13 OR 16 digits in them.
Cards issued by American Express will ALWAYS have the first two digits of 34 or 37
and will always contain 15 digits.
Cards issued by Mastercard will ALWAYS be 16 digits and will ALWAYS have the
first two digits between 51-55 (inclusive) OR will have the first four digits
between 2221-2720 (inclusive)
Modify your redact_card_numbers function to only redact valid Mastercard, Visa, or
American Express credit card numbers. Like the previous part, the redaction will replace
all of the digits with an “x” character EXCEPT for the last 4 digits.
Examples
// No credit card found, no transformation needed
redact_card_numbers("basic_string 12345 no redaction")
returns "basic_string 12345 no redaction"
// 16 digit number does not get redacted as it does not match brand criteria
redact_card_numbers("1234567890123456 is not a card")
returns "1234567890123456 is not a card"
// 16 digit number Visa does get redacted as it matches brand criteria
redact_card_numbers("4234567890123456 is a valid visa")
returns "xxxxxxxxxxxx3456 is a valid visa"
'''
import unittest

def is_valid_credit_card(token):
    if token.startswith('4') and (len(token)==13 or len(token)==16): #visa
        return True
    if (token.startswith('34') or  token.startswith('37')) and len(token)==15: #amex
        return True
    if len(token)==16 and (51<=int(token[:2])<=55 or 2221<=int(token[:4])<=2720):
        return True
    return False

def redact_card_numbers(card_string):
    tokens=card_string.split(" ")
    redact_token=[]
    for token in tokens:
        if token.isdigit() and is_valid_credit_card(token):
            new_token='x'*(len(token)-4)+token[-4:]
            redact_token.append(new_token)
        else:
            redact_token.append(token)
    return " ".join(redact_token)

print(redact_card_numbers("1234567890123456 is a number"))
print(redact_card_numbers("basic_string 12345 no redaction"))  # "basic_string 12345 no redaction"
print(redact_card_numbers("1234567890123456 is not a card"))  # "1234567890123456 is not a card"
print(redact_card_numbers("4234567890123456 is a valid visa"))  # "xxxxxxxxxxxx3456 is a valid visa"
print(redact_card_numbers("341234567890123 is a valid amex"))  # "xxxxxxxxxxx0123 is a valid amex"
print(redact_card_numbers("371234567890123 is a valid amex"))  # "xxxxxxxxxxx0123 is a valid amex"
print(redact_card_numbers("5112345678901234 is a valid mastercard"))  # "xxxxxxxxxxxx1234 is a valid mastercard"
print(redact_card_numbers("2222345678901234 is a valid mastercard"))  # "xxxxxxxxxxxx1234 is a valid mastercard"
print(redact_card_numbers("2720345678901234 is a valid mastercard"))  # "xxxxxxxxxxxx1234 is a valid mastercard"

class TestRedactToken(unittest.TestCase):
    
    def test_no_redaction_needed(self):
        self.assertEqual(redact_card_numbers("basic_string 12345 no redaction"), "basic_string 12345 no redaction")

    def test_non_matching_16_digit_number(self):
        self.assertEqual(redact_card_numbers("1234567890123456 is not a card"), "1234567890123456 is not a card")

    def test_16_digit_visa(self):
        self.assertEqual(redact_card_numbers("4234567890123456 is a valid visa"), "xxxxxxxxxxxx3456 is a valid visa")

    def test_13_digit_visa(self):
        self.assertEqual(redact_card_numbers("4234567890123 is a valid visa"), "xxxxxxxxx0123 is a valid visa")

    def test_15_digit_amex_34(self):
        self.assertEqual(redact_card_numbers("341234567890123 is a valid amex"), "xxxxxxxxxxx0123 is a valid amex")

    def test_15_digit_amex_37(self):
        self.assertEqual(redact_card_numbers("371234567890123 is a valid amex"), "xxxxxxxxxxx0123 is a valid amex")

    def test_16_digit_mastercard_51_55(self):
        self.assertEqual(redact_card_numbers("5112345678901234 is a valid mastercard"),
                         "xxxxxxxxxxxx1234 is a valid mastercard")

    def test_16_digit_mastercard_2221_2720(self):
        self.assertEqual(redact_card_numbers("2222345678901234 is a valid mastercard"),
                         "xxxxxxxxxxxx1234 is a valid mastercard")
        self.assertEqual(redact_card_numbers("2720345678901234 is a valid mastercard"),
                         "xxxxxxxxxxxx1234 is a valid mastercard")

    def test_multiple_credit_cards(self):
        self.assertEqual(redact_card_numbers("multiple cards 4234567890123 5112345678901234"),
                         "multiple cards xxxxxxxxx0123 xxxxxxxxxxxx1234")

    def test_non_digit_tokens(self):
        self.assertEqual(redact_card_numbers("string with special $%@# characters 4234567890123456"),
                         "string with special $%@# characters xxxxxxxxxxxx3456")

    def test_mixed_tokens(self):
        self.assertEqual(redact_card_numbers("text 4234567890123 more text 371234567890123 more text"),
                         "text xxxxxxxxx0123 more text xxxxxxxxxxx0123 more text")

    # Run the tests


if __name__ == '__main__':
    unittest.main()
