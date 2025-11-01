import Service.functionalities as Func
import UI.menu_functions as Menu
import UI.input_functions as Input
import Service.Add_functions as Add
import Service.undo_functions as Undo
import Service.Delete_functions as Delete


def run_app(apartments, utilities):
    home_option(apartments, utilities)


def home_option(apartments, utilities):
    """
    This function print home menu
    Args:
        apartments:
        utilities:

    Returns:

    """
    while True:
        Menu.home_menu()
        option = Input.input_option(1, 7) - 1
        if option == 0:
            add_option(apartments, utilities)
        elif option == 1:
            delete_option(apartments, utilities)
        elif option == 2:
            search_option(apartments, utilities)
        elif option == 3:
            filter_option(apartments, utilities)
        elif option == 4:
            raports_option(apartments, utilities)
        elif option == 5:
            break
        elif option == 6:
            Undo.undo(apartments, utilities)


def add_option(apartments, utilities):
    """
    This function print Add menu
    Args:
        apartments:
        utilities:

    Returns:

    """
    options = [Menu.new_add_menu, Menu.new_add_menu]
    while True:
        Menu.add_menu()
        option = Input.input_option(1, 4) - 1
        if option == 2:
            break
        if option == 3:
            Undo.undo(apartments, utilities)
        else:
            [year, month, day, number, type, subtype, amount] = options[option]()
            Add.add_day_utilities(utilities, number, type, subtype, amount, year, month, day)
            Add.set_expenses(apartments, number, type, subtype, amount)
            Menu.print_expenses(year, month, day, number, type, subtype, amount)
            Func.stay(3)


def delete_option(apartments, utilities):
    """
    This function print Delete menu
    Args:
        apartments:
        utilities:

    Returns:

    """
    options = [Menu.delete_all_expenses, Menu.delete_consecutive_expenses, Menu.delete_a_type]
    while True:
        Menu.delete_menu()
        option = Input.input_option(1, 5) - 1
        if option == 3:
            break
        if option == 4:
            Undo.undo(apartments, utilities)
        else:
            if option == 0:
                number = options[option]()
                Delete.delete_all_expenses(apartments, number=number)
            elif option == 1:
                [start, end] = options[option]()
                Delete.delete_expenses_consecutive_apartments(apartments, start, end)
            elif option == 2:
                [type, subtype] = options[option]()
                Delete.delete_expenses(apartments, type=type, subtype=subtype)


def search_option(apartments, utilities):
    """
    This function print Search menu
    Args:
        apartments:
        utilities:

    Returns:

    """
    options = [Menu.search_greater, Menu.search_type, Menu.search_by_day]
    while True:
        Func.clear()
        Menu.search_menu()
        option = Input.input_option(1, 5) - 1
        if option == 3:
            break
        elif option == 4:
            Undo.undo(apartments, utilities)
        else:
            options[option](apartments, utilities)


def filter_option(apartments, utilities):
    """
        This function print filter menu
    Args:
        apartments:
        utilities:

    Returns:

    """
    options = [Menu.filter_by_type, Menu.filter_by_sum]
    while True:
        Func.clear()
        Menu.filter_menu()
        option = Input.input_option(1, 4) - 1
        if option == 2:
            break
        elif option == 3:
            Undo.undo(apartments, utilities)
        else:
            options[option](apartments, utilities)


def raports_option(apartments, utilities):
    """
    This function print raports menu
    Args:
        apartments:
        utilities:

    Returns:

    """
    options = [Menu.total_amount_type, Menu.sorted_by_type, Menu.total_amount_apart]
    while True:
        Func.clear()
        Menu.raports_menu()
        option = Input.input_option(1, 5) - 1
        if option == 3:
            break
        elif option == 4:
            Undo.undo(apartments, utilities)
        else:
            options[option](apartments, utilities)
