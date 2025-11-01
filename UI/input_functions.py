import UI.menu_functions as Print


def input_option(left, right):
    """
    This function read the option that must be in range[left,right]
    Args:
        left:
        right:

    Returns:

    """
    while True:
        value = input("Select an option: ")
        try:
            user_command = int(value)
            if not (left <= user_command <= right):
                raise ValueError
            break
        except ValueError:
            Print.option_error(left, right)
    return user_command


def input_number(text):
    """
    This function read an integer number
    Args:
        text:

    Returns:

    """
    while True:
        value = input(text)
        try:
            user_command = int(value)
            break
        except ValueError:
            Print.details_error("Oops.. You must enter a number!")
    return user_command


def input_text(text1):
    """
    This function read an input text
    Args:
        text1:

    Returns:

    """
    text = input(text1)
    return text
