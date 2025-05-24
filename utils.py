# utils.py
# Utility functions: for input validation and print decorations

def print_line():
    print("-" * 30)
    # Print a separation line for better display

def input_choice(prompt, choices):
    """
    Get user input until a valid option is entered.
    :param prompt: The input prompt to show the user
    :param choices: A list of valid choices (as strings)
    :return: The chosen value as a string
    """
    while True:
        val = input(prompt).strip()
        if val in choices:
            return val
        else:
            print(f"Please enter one of {choices}")
