import Service.functionalities as func


def set_expenses(apartments, number, type, subtype, amount):
    """_summary_

        This function set the amount value in list at that index with the provided type and subtype

    Args:
        apartments (list): a list with two list where the first list is the current data of expanses and
                           the second list is the previous data of expenses for apartments
        number (int): the apartment numbers
        type (string): type of expenses
        subtype (string): type of expenses
        amount (int): the amount of money that need to be paid
    """
    index = number - 1
    apartments[1].append([func.copy_element(utility) for utility in apartments[0]])
    apartments[0][index][type][subtype] = amount


def add_day_utilities(utilities, number, type, subtype, amount, year, month, day):
    """
     This function add the new expenses in history of expenses
    Args:
        utilities:
        number:
        type:
        subtype:
        amount:
        year:
        month:
        day:

    Returns:

    """
    date = "/".join(str(x) for x in [year, month, day])
    utilities[1].append(func.copy_element(utilities[0]))
    utilities[0][date].append({type: {subtype: amount}, 'number': number})
