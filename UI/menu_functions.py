import UI.Print_functions as Print
import Service.functionalities as Func
import UI.input_functions as Input
import Service.Filter_functions as Filter


def home_menu():
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Home Menu")
    Print.print_blank_line()
    Print.print_two_option("Add (1)", "Delete (2)")
    Print.print_blank_line()
    Print.print_two_option("Search (3)", "Filter (4)")
    Print.print_blank_line()
    Print.print_one_button("Reports (5)")
    Print.print_blank_line()
    Print.print_buttons("QUIT (6)", "UNDO (7)")
    Print.print_blank_line()
    Print.print_border()


def add_menu():
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Add Expenses Menu")
    Print.print_blank_line()
    Print.print_two_option("Add (1)", "Change (2)")
    Print.print_blank_line()
    Print.print_buttons("BACK (3)", "UNDO (4)")
    Print.print_blank_line()
    Print.print_border()


def check_type(type, subtype):
    subtypes = [["electricity", "gas"], ["monitoring", "guard"], ["cleaning", "maintenance"]]
    if type == "utilities":
        for sub in subtypes[0]:
            if subtype == sub:
                return True
    elif type == "security":
        for sub in subtypes[1]:
            if subtype == sub:
                return True
    elif type == "building":
        for sub in subtypes[2]:
            if subtype == sub:
                return True
    return False


def check_date(month, day):
    if not (1 <= int(month) <= 12):
        return False
    if not (1 <= int(day) <= 31):
        return False
    return True


def new_add_menu():
    need = ["Add year:", "Add month:", "Add day: ", "Add number of apartment:", "Add type of expenses:",
            "Add subtype of expenses:", "Add amount of expenses:"]
    need_input = ["Add year:", "Add month(1-12):", "Add day(1-31): ", "Add number of apartment(1-20):",
                  "Add type of expenses(utilities,security,building)",
                  "Add subtype of expenses(electricity,gas,guard,monitoring,cleaning,maintenance):",
                  "Add amount of expenses:"]

    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Add New Expenses Menu")
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_blank_line()
        [year, month, day, number, type, subtype, amount] = input_expenses(need, need_input)
        number = int(number)
        amount = int(amount)
        if check_type(type, subtype) and check_date(month, day) and (1 <= number <= 20):
            return [year, month, day, number, type, subtype, amount]
        details_error("Oops you entered invalid options!")
        Func.stay(3)


def delete_menu():
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Delete Expenses Menu")
    Print.print_blank_line()
    Print.print_one_button("Delete all expenses from an apartment (1)")
    Print.print_blank_line()
    Print.print_one_button("Delete expenses from consecutive apartments (2)")
    Print.print_blank_line()
    Print.print_one_button("Delete a type of expenses from all apartments (3)")
    Print.print_blank_line()
    Print.print_buttons("BACK (4)", "UNDO (5)")
    Print.print_blank_line()
    Print.print_border()


def delete_all_expenses():
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Delete Expenses Menu")
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_blank_line()
        number = Input.input_text("Enter the number of apartment you wish to delete the expenses from(1-20): ")
        number = int(number)
        good = True
        if not (1 <= number <= 20):
            good = False

        if good:
            return number
        details_error("Oops you entered an invalid number!")
        Func.stay(2)


def delete_consecutive_expenses():
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Delete Expenses Menu")
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_one_button("The start number must be smaller than the end number!!")
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_blank_line()

        number1 = Input.input_text("Enter the number where you want to start(1-20): ")
        number1 = int(number1)

        number2 = Input.input_text("Enter the number where you want to stop(1-20): ")
        number2 = int(number2)

        good = True
        if not (1 <= number1 <= 20):
            good = False

        if not (1 <= number2 <= 20):
            good = False

        if number1 >= number2:
            good = False

        if good:
            return [number1, number2]
        details_error("Oops you entered an invalid number!")
        Func.stay(2)


def delete_a_type():
    subtypes = [["electricity", "gas"], ["monitoring", "guard"], ["cleaning", "maintenance"]]
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Delete Expenses Menu")
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_one_button("The type and subtype of expenses must be: ")
        Print.print_blank_line()
        text = ", ".join(str(sub) for sub in subtypes[0])
        Print.print_centered_text("utilities: " + text)
        Print.print_blank_line()
        text = ", ".join(str(sub) for sub in subtypes[1])
        Print.print_centered_text("security: " + text)
        Print.print_blank_line()
        text = ", ".join(str(sub) for sub in subtypes[2])
        Print.print_centered_text("building: " + text)
        Print.print_blank_line()
        Print.print_blank_line()

        type = Input.input_text("Enter the type of expenses you wish to delete: ")
        subtype = Input.input_text("Enter the subtype of expenses you wish to delete: ")

        if check_type(type, subtype):
            return [type, subtype]
        details_error("Oops you entered an invalid type or subtype!")
        Func.stay(2)


def print_expenses(year, month, day, number, type, subtype, amount):
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("You add an expenses successfully")
    Print.print_blank_line()
    Print.print_blank_line()
    Print.print_centered_text("Year: " + year)
    Print.print_centered_text("Month: " + month)
    Print.print_centered_text("Day: " + day)
    Print.print_centered_text("number: " + str(number))
    Print.print_centered_text("type: " + type)
    Print.print_centered_text("subtype: " + subtype)
    Print.print_centered_text("amount: " + str(amount))
    Print.print_blank_line()
    Print.print_border()


def option_error(left, right):
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Oops you entered an invalid option!")
    Print.print_blank_line()
    Print.print_blank_line()
    Print.print_centered_text("You must enter a valid option between: " + str(left) + " and " + str(right))
    Print.print_blank_line()
    Print.print_blank_line()
    Print.print_border()


def details_error(text):
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text(text)
    Print.print_blank_line()
    Print.print_blank_line()
    Print.print_centered_text("Please try again: ")
    Print.print_blank_line()
    Print.print_blank_line()
    Print.print_border()


def print_table(apartments, numbers):
    totals = Func.calc_expenses(apartments)
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Apartments table")
        Print.print_blank_line()
        Print.print_table_header()
        for number in numbers:
            print_apartment(apartments, number, totals[number])

        Print.print_button("BACK (1)")
        Print.print_blank_line()
        Print.print_border()
        option = Input.input_option(1, 1)
        if option == 1:
            break


def print_apartment(apartments, number, total):
    Print.print_table_row(apartments=apartments, number=number, total=total)
    Print.print_border()


def search_menu():
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Search Menu")
    Print.print_blank_line()
    Print.print_one_button("Print apartments with expenses greater than 'value' (1)")
    Print.print_blank_line()
    Print.print_one_button("Print expenses type (2)")
    Print.print_blank_line()
    Print.print_one_button("Print all expenses until 'day' and greater than 'value' (3)")
    Print.print_blank_line()
    Print.print_buttons("BACK (4)", "UNDO (5)")
    Print.print_blank_line()
    Print.print_border()


def search_greater(apartments, utilities):
    totals = Func.calc_expenses(apartments)
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Search Menu")
    Print.print_blank_line()
    Print.print_one_button("Add a value: ")
    Print.print_blank_line()
    Print.print_blank_line()
    value = Input.input_number("Add a value:")
    Print.print_blank_line()
    Print.print_blank_line()
    Print.print_border()
    numbers = []
    for ind in range(0, len(totals)):
        if totals[ind] >= value:
            numbers.append(ind)

    if len(numbers) == 0:
        details_error("Doesn't exist apartments with expenses greater than 'value'!")
        Func.stay(3)
    else:
        print_table(apartments, numbers)


def search_type(apartments, utilities):
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Search Menu")
        Print.print_blank_line()
        Print.print_one_button("Add type and subtype: ")
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_border()
        type = Input.input_text("Add type: ")
        subtype = Input.input_text("Add subtype: ")

        if check_type(type, subtype):
            print_expenses_table(apartments, type, subtype)
            break

        details_error("You entered an invalid type or subtype")
        Func.stay(3)


def print_expenses_table(apartments, type, subtype):
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Apartments table")
        Print.print_blank_line()
        Print.print_expenses_header()
        for number in range(1, 21):
            Print.print_expenses_table(apartments, number, type, subtype)
        Print.print_blank_line()
        Print.print_button("BACK (1)")
        Print.print_blank_line()
        Print.print_border()
        option = Input.input_option(1, 1)
        if option == 1:
            break


def input_expenses(need, need_input):
    expenses = []
    contor = 0
    while contor < len(need):
        Func.clear()
        Print.print_one_button(need[contor])
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_blank_line()
        Print.print_border()

        exp = Input.input_text(need_input[contor])
        expenses.append(exp)
        contor += 1
    return expenses


def search_by_add_input():
    need_input = ["Add year:", "Add month(1-12):", "Add day(1-31): ", "Add amount: "]
    need = ["Add year:", "Add month:", "Add day: ", "Add amount: "]
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_centered_text("Search Menu")
        Print.print_blank_line()
        [year, month, day, sum] = input_expenses(need, need_input)
        if check_date(month, day):
            return [year, month, day, sum]
        details_error("Oops you entered invalid options!")
        Func.stay(3)


def search_by_day(apartments, utilities):
    [year, month, day, sum] = search_by_add_input()
    date = "/".join(str(x) for x in [year, month, day])

    Func.clear()
    while True:
        Print.print_border()
        Print.print_blank_line()
        Print.print_one_button("Expenses before " + date + " and the value of amount greater than " + sum)
        Print.print_blank_line()
        Print.print_search_table_header(date, sum)
        if (len(utilities[0]) > 0):
            for data in sorted(utilities[0].keys()):
                if data <= date:
                    for index in range(0, len(utilities[0][data])):
                        record = utilities[0][data][index]
                        type_, el = next((k, v) for k, v in record.items() if isinstance(v, dict))
                        for subtype, amount in el.items():
                            number = record["number"]
                            if amount > int(sum):
                                Print.print_search_table_row(data, number, type_, subtype, amount)

        Print.print_blank_line()
        Print.print_button("BACK (1)")
        Print.print_blank_line()
        Print.print_border()

        option = Input.input_option(1, 1)
        if option == 1:
            break


def filter_by_type(apartments, utilities):
    need_input = ["Add type:", "Add subtype:"]
    need = ["Add type:", "Add subtype:"]
    [type, subtype] = input_expenses(need, need_input)
    Filter.filter_by_type(apartments, subtype)
    numbers = []
    for index in range(0, 20):
        numbers.append(index)
    print_table(apartments, numbers)


def filter_by_sum(apartments, utilities):
    need_input = ["Add amount: "]
    need = ["Add amount:"]
    [amount] = input_expenses(need, need_input)
    amount = int(amount)
    filtered_apart = Filter.filter_by_amount(apartments, amount)
    numbers = []
    for index in range(0, 20):
        numbers.append(index)
    print_table(apartments, numbers)


def filter_menu():
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Filter Expenses Menu")
    Print.print_blank_line()
    Print.print_one_button("Filter by type (1)")
    Print.print_blank_line()
    Print.print_one_button("Filter by sum (2)")
    Print.print_blank_line()
    Print.print_buttons("BACK (3)", "UNDO (4)")
    Print.print_blank_line()
    Print.print_border()


def total_amount_type(apartments, utilities):
    need_input = ["Add type:", "Add subtype:"]
    need = ["Add type:", "Add subtype:"]
    [type, subtype] = input_expenses(need, need_input)
    total = 0
    for index in range(0, 20):
        total += apartments[0][index][type][subtype]

    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_one_button("Total Amount: " + str(total))
        Print.print_blank_line()
        Print.print_button("BACK (1)")
        Print.print_blank_line()
        Print.print_border()
        option = Input.input_option(1, 1)
        if option == 1:
            break


def sorted_by_type(apartments, utilities):
    need_input = ["Add type:", "Add subtype:"]
    need = ["Add type:", "Add subtype:"]
    [type, subtype] = input_expenses(need, need_input)
    sorted_apartments = Func.sort_apartments_by(apartments, type, subtype)
    numbers = []
    for index in range(0, 20):
        numbers.append(index)
    print_table(sorted_apartments, numbers)


def total_amount_apart(apartments, utilities):
    need_input = ["Add number: "]
    need = ["Add number: "]
    [number] = input_expenses(need, need_input)
    number = int(number)
    totals = Func.calc_expenses(apartments)
    while True:
        Func.clear()
        Print.print_border()
        Print.print_blank_line()
        Print.print_one_button("Total Amount: " + str(totals[number - 1]))
        Print.print_blank_line()
        Print.print_button("BACK (1)")
        Print.print_blank_line()
        Print.print_border()
        option = Input.input_option(1, 1)
        if option == 1:
            break


def reports_menu():
    Func.clear()
    Print.print_border()
    Print.print_blank_line()
    Print.print_centered_text("Reports Menu")
    Print.print_blank_line()
    Print.print_one_button("Print total sum of a specific type (1)")
    Print.print_blank_line()
    Print.print_one_button("Print apartments sorted by a specific type (2)")
    Print.print_blank_line()
    Print.print_one_button("Print total sum of an apartment (3)")
    Print.print_blank_line()
    Print.print_buttons("BACK (4)", "UNDO (5)")
    Print.print_blank_line()
    Print.print_border()
