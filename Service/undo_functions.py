import Service.functionalities as func


def undo(apartments, utilities):
    """_summary_

        This function undo the last operation that user does
    Args:
        apartments (list): a list with two list where the first list is the current data of expanses and
                           the second list is the previous data of expenses for apartments
    """
    if len(apartments[1]) > 0:
        previous = [func.copy_element(utility) for utility in apartments[1][-1]]
        apartments[1].pop(len(apartments[1]) - 1)
        apartments[0] = [func.copy_element(utility) for utility in previous]

    if len(utilities[1]) > 0:
        previous = [func.copy_element(utility) for utility in utilities[1][-1]]
        utilities[1].pop(len(utilities[1]) - 1)
        utilities[0] = [func.copy_element(utility) for utility in previous]
