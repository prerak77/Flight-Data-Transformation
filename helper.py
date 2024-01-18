import string

# This functions will remove any punctiuactions but it will not remove any numbers


def remove_punctuation(input_string):
    # Create a string containing all punctuation characters
    punctuations = string.punctuation

    # Use a loop to remove each punctuation character from the input string
    cleaned_string = ''.join(
        char for char in input_string if char not in punctuations)

    return cleaned_string

# This functions will remove any numbers present in the string


def remove_numbers(input_string):
    # Create a translation table to remove digits
    translation_table = str.maketrans("", "", string.digits)

    # Apply the translation table to the input string
    cleaned_string = input_string.translate(translation_table)

    return cleaned_string
