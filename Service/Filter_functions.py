import Service.functionalities as func


def filter_by_type(apartments, subtype):
    """
    This function return a list of apartments filtered by subtype
    Args:
        apartments:
        subtype:

    Returns:

    """
    lista = [func.copy_element(apartments[0], subtype=subtype)]
    return lista


def filter_by_amount(apartments, amount):
    """
    This function return a list of apartments filtered by amount
    Args:
        apartments:
        amount:

    Returns:

    """
    lista = [[func.copy_element(utility, amount=amount) for utility in apartments[0]]]
    return lista
