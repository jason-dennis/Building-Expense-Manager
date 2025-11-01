import Service.functionalities as func


def delete_all_expenses(apartments, utilities, floor=0, number=0):
    """_summary_

        This function delete all expenses from a specific apartment

    Args:
        apartments (list): a list with two list where the first list is the current data of expanses and
                           the second list is the previous data of expenses for apartments
        floor (int): the floor number of the apartments
        number (int): the apartment numbers
    """
    index = number - 1
    floor = apartments[0][number - 1]['floor']
    apartments[1].append([func.copy_element(utility) for utility in apartments[0]])
    apartments[0][index] = func.init_apartment(floor, number)


def delete_expenses(apartments, utilities, type, subtype):
    """_summary_
        This function delete a specific type of expenses from all apartments
    Args:
        apartments (list): a list with two list where the first list is the current data of expanses and
                           the second list is the previous data of expenses for apartments
        type (string): type of expenses
        subtype (string): type of expenses
    """
    apartments[1].append([func.copy_element(utility) for utility in apartments[0]])
    for index in range(0, len(apartments[0])):
        apartments[0][index][type][subtype] = 0

    utilities[1].append(func.copy_element(utilities[0]))
    for date in list(utilities[0].keys()):
        utilities[0][date] = [
            record for record in utilities[0][date]
            if subtype not in record.get(type, {})
        ]


def delete_expenses_consecutive_apartments(apartments, utilities, first_index, last_index):
    """_summary_
        This function delete all expenses from apartments with number in range[first_index:last_index]
    Args:
        apartments (list): a list with two list where the first list is the current data of expanses and
                           the second list is the previous data of expenses for apartments
        first_index (int): the apartment number from where we start to delete all expenses
        last_index (int): the apartment number where we end to delete all expenses
    """
    for index in range(first_index, last_index + 1):
        floor = (index // 5) + 1
        delete_all_expenses(apartments, utilities, floor, index)
        for date in list(utilities[0].keys()):
            utilities[0][date] = [
                record for record in utilities[0][date]
                if not (
                        record.get("number") == index
                )
            ]
