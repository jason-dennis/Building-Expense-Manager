from collections import defaultdict

import Service.Add_functions as Add
import Service.Delete_functions as Delete
import Service.Filter_functions as Filter
import Service.functionalities as Func
import Service.undo_functions as Undo


def test_delete_expenses():
    """_summary_

        Test function for delete expenses functions
    """
    apartments = Func.create_apartments()
    utilities = [defaultdict(list), []]

    # ---------- delete all expenses from apartment 3 ----------
    Add.set_expenses(apartments, 3, "utilities", "electricity", 15)
    Add.set_expenses(apartments, 3, "utilities", "gas", 30)
    Add.set_expenses(apartments, 3, "utilities", "gas", 105)
    Add.set_expenses(apartments, 3, "security", "monitoring", 50)
    Add.set_expenses(apartments, 3, "building", "cleaning", 5)

    Delete.delete_all_expenses(apartments, utilities, 1, 3)
    assert Func.get_utility_amount(apartments, 3, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 3, "utilities", "gas") == 0
    assert Func.get_utility_amount(apartments, 3, "utilities", "gas") == 0
    assert Func.get_utility_amount(apartments, 3, "security", "monitoring") == 0
    assert Func.get_utility_amount(apartments, 3, "building", "cleaning") == 0

    # ---------- delete all electricity expenses from all apartments ----------

    Add.set_expenses(apartments, 3, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 4, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 5, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 6, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 7, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 12, "utilities", "electricity", 34)

    Delete.delete_expenses(apartments, utilities, "utilities", "electricity")

    assert Func.get_utility_amount(apartments, 3, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 4, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 5, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 6, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 7, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 12, "utilities", "electricity") == 0

    # ---------- delete all expenses from apartments 2-4 and 6-7 ----------

    Add.set_expenses(apartments, 2, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 3, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 4, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 5, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 6, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 7, "utilities", "electricity", 34)

    Delete.delete_expenses_consecutive_apartments(apartments, utilities, 2, 4)
    Delete.delete_expenses_consecutive_apartments(apartments, utilities, 6, 7)

    assert Func.get_utility_amount(apartments, 2, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 3, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 4, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 5, "utilities", "electricity") == 34
    assert Func.get_utility_amount(apartments, 6, "utilities", "electricity") == 0
    assert Func.get_utility_amount(apartments, 7, "utilities", "electricity") == 0


def test_set_expenses():
    """_summary_

        Test function for set_expenses
    """
    apartments = Func.create_apartments()

    # ---------- set expenses for apartment 3 ----------

    Add.set_expenses(apartments, 3, "utilities", "electricity", 15)
    Add.set_expenses(apartments, 3, "utilities", "gas", 30)
    Add.set_expenses(apartments, 3, "utilities", "electricity", 105)
    Add.set_expenses(apartments, 3, "security", "monitoring", 50)
    Add.set_expenses(apartments, 3, "building", "cleaning", 5)

    assert Func.get_utility_amount(apartments, 3, "utilities", "gas") == 30
    assert Func.get_utility_amount(apartments, 3, "utilities", "electricity") == 105
    assert Func.get_utility_amount(apartments, 3, "security", "monitoring") == 50
    assert Func.get_utility_amount(apartments, 3, "building", "cleaning") == 5

    Add.set_expenses(apartments, 3, "utilities", "electricity", 34)
    Add.set_expenses(apartments, 3, "utilities", "gas", 31)

    assert Func.get_utility_amount(apartments, 3, "utilities", "electricity") == 34
    assert Func.get_utility_amount(apartments, 3, "utilities", "gas") == 31


def test_undo():
    """
    This function test Undo Function
    Returns:

    """
    apartments = Func.create_apartments()
    utilities = [defaultdict(list), []]

    Add.set_expenses(apartments, 3, "utilities", "electricity", 15)
    Add.set_expenses(apartments, 3, "utilities", "gas", 30)
    Add.set_expenses(apartments, 3, "utilities", "electricity", 34)

    Undo.undo(apartments, utilities)

    assert Func.get_utility_amount(apartments, 3, "utilities", "electricity") == 15
    assert Func.get_utility_amount(apartments, 3, "utilities", "gas") == 30

    Add.set_expenses(apartments, 3, "utilities", "gas", 34)
    Add.set_expenses(apartments, 3, "utilities", "electricity", 34)
    Delete.delete_all_expenses(apartments, utilities, 1, 3)

    Undo.undo(apartments, utilities)

    assert Func.get_utility_amount(apartments, 3, "utilities", "electricity") == 34
    assert Func.get_utility_amount(apartments, 3, "utilities", "gas") == 34


def test_filter_by_type():
    """
    This function test filter_by_type function
    Returns:

    """
    apartments = Func.create_apartments()
    Add.set_expenses(apartments, 3, "utilities", "electricity", 15)
    Add.set_expenses(apartments, 3, "utilities", "gas", 30)
    Add.set_expenses(apartments, 3, "security", "monitoring", 50)
    Add.set_expenses(apartments, 3, "building", "cleaning", 5)

    filtered_apart = Filter.filter_by_type(apartments, "electricity")
    assert filtered_apart[2]['utilities']['electricity'] == 0


def test_filter_by_amount():
    """
    This function test filter_by_amount function
    Returns:

    """
    apartments = Func.create_apartments()
    Add.set_expenses(apartments, 3, "utilities", "electricity", 150)
    Add.set_expenses(apartments, 3, "utilities", "gas", 30)
    Add.set_expenses(apartments, 3, "security", "monitoring", 50)
    Add.set_expenses(apartments, 3, "building", "cleaning", 5)

    filtered_apart = Filter.filter_by_amount(apartments, 100)
    assert filtered_apart[2]['utilities']['gas'] == 0


def test_add_day_utilities():
    """
    This function Test add_day_utilities function
    Returns:

    """
    utilities = [defaultdict(list), []]
    Add.add_day_utilities(utilities, 10, "utilities", "electricity", 20, 2025, 10, 21)
    Add.add_day_utilities(utilities, 15, "utilities", "electricity", 10, 2025, 10, 18)
    Add.add_day_utilities(utilities, 12, "utilities", "gas", 30, 2025, 10, 21)
    Add.add_day_utilities(utilities, 2, "utilities", "gas", 25, 2025, 10, 18)

    assert utilities[0]["2025/10/21"][-1] == {'utilities': {'gas': 30}, 'number': 12}
    assert utilities[0]["2025/10/18"][-1] == {'utilities': {'gas': 25}, 'number': 2}

    assert utilities[0]["2025/10/21"][-2] == {'utilities': {'electricity': 20}, 'number': 10}
    assert utilities[0]["2025/10/18"][-2] == {'utilities': {'electricity': 10}, 'number': 15}


def test():
    test_add_day_utilities()
    test_filter_by_amount()
    test_filter_by_type()
    test_undo()
    test_set_expenses()
    test_delete_expenses()
