def sum_of_digits(s):
    if not s:  # Check if the string is empty or None
        print('Empty string entered!')
        return 0

    sum_digits = 0
    non_digits = []  # List to hold non-digit characters
    digits_operation = []  # List to hold digits for operation string

    for char in s:
        if char.isdigit():  # Check if the character is a digit
            sum_digits += int(char)
            digits_operation.append(char)
        else:
            non_digits.append(char)

    if digits_operation:
        # Print operation string for digits
        print('The sum of digits operation performs ' + ' + '.join(digits_operation))
    else:
        print('The sum of digits operation could not detect a digit!')

    if non_digits:
        print('The extracted non-digits are:', non_digits)
    else:
        print('The extracted non-digits are: []')

    return sum_digits

# Test cases
print(sum_of_digits("123"))  # Expected: 6
print(sum_of_digits("we10a20b"))  # Expected: 3
print(sum_of_digits("united"))  # Expected: 0
print(sum_of_digits(""))  # Expected: 0
