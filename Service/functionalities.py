import os
import time


def init_apartment(floor, number):
    """_summary_

        This function returns the expenses details for a specific apartment with all expenses 0
    Args:
        floor (int): the floor number of the apartments
        number (int): the apartment numbers
    Returns:
        dict: a dictionary with the expenses details
    """
    return {
        "floor": floor,
        "number": number,
        "utilities": {"electricity": 0, "gas": 0},
        "security": {"monitoring": 0, "guard": 0},
        "building": {"cleaning": 0, "maintenance": 0}
    }


def create_apartments():
    """_summary_

        This function create for each apartment the expenses details

    Returns:
        list : a list where each element is a dictionary with expenses details
    """
    apartments = [[], []]
    for floor in range(1, 5):
        for number in range(1, 6):
            apartments[0].append(init_apartment(floor, (floor - 1) * 5 + number))

    return apartments


def copy_element(element, subtype="", amount=-100000):
    """_summary_
        This function copy an element
    """
    if isinstance(element, dict):
        return {name: (0 if name == subtype else copy_element(el, subtype, amount))
                for name, el in element.items()}
    if isinstance(element, list):
        return [copy_element(x, subtype, amount) for x in element]
    if isinstance(element, (int, float)) and element < amount:
        return 0
    return element


def get_utility_amount(apartments, number, type, subtype):
    """_summary_

        This function return the value that is storage in list at that index with the provided type and subtype

    Args:
        apartments (list): a list with two list where the first list is the current data of expanses and
                           the second list is the previous data of expenses for apartments
        number (int): the apartment numbers
        type (string): type of expenses
        subtype (string): type of expenses

    Returns:
        int : utility amount for a specific apartment.
    """
    index = number - 1
    return apartments[0][index][type][subtype]


def calc_expenses(apartments):
    """
    This function return a list with sum of amount of every type of expenses for each apartment
    Args:
        apartments:

    Returns:

    """
    type = ['utilities', 'security', 'building']
    subtypes = [["electricity", "gas"], ["monitoring", "guard"], ["cleaning", "maintenance"]]
    totals = []
    for number in range(1, 21):
        total = 0
        for tip in range(0, 3):
            for sub in subtypes[tip]:
                total += apartments[0][number - 1][type[tip]][sub]
        totals.append(total)
    return totals


def sort_apartments_by(apartments, type, subtype):
    """
    This function sorts the apartments by their respective type
    Args:
        apartments:
        type:
        subtype:

    Returns:

    """
    return [sorted(apartments[0], key=lambda x: x[type][subtype])]


def clear():
    """
    This function clears the screen
    Returns:

    """
    os.system('clear')


def stay(seconds):
    """
    This function froze the screen
    Args:
        seconds:

    Returns:

    """
    time.sleep(seconds)
