import shutil

terminal_width = shutil.get_terminal_size().columns
box_size = terminal_width // 4
begin_space = box_size // 2
between_space = box_size // 2
end_space = box_size // 2


# 2*box+box+box/2+box/2=4box= terminal_width

def print_border(border="#"):
    print(border * terminal_width)


def print_two_option(text1, text2, border="#"):
    print(border
          + "{:^{w}}".format(border * box_size, w=2 * box_size)
          + "{:^{w}}".format(border * box_size, w=2 * box_size - 1)
          + border)

    print(border
          + "{:>{w}}".format(border, w=begin_space + 1)
          + "{:^{w}}".format(text1, w=box_size - 2)
          + "{:<{w}}".format(border, w=between_space + 1)
          + "{:>{w}}".format(border, w=between_space + 2)
          + "{:^{w}}".format(text2, w=box_size - 2)
          + "{:<{w}}".format(border, w=end_space + 1)
          + border)

    print(border
          + "{:^{w}}".format(border * box_size, w=2 * box_size)
          + "{:^{w}}".format(border * box_size, w=2 * box_size - 1)
          + border)


def print_blank_line(border="#"):
    print(border
          + "{:^{w}}".format(" ", w=terminal_width - 2)
          + border)


def print_centered_text(text, border="#"):
    print(border +
          "{:^{w}}".format(text, w=terminal_width - 2)
          + border)


def print_buttons(text1, text2, border="#"):
    print(border
          + "{:^{w}}".format(border * begin_space, w=box_size)
          + "{:^{w}}".format("", w=2 * box_size - 1)
          + "{:^{w}}".format(border * begin_space, w=box_size)
          + border)

    print(border
          + "{:>{w}}".format(border, w=begin_space // 2 + 2)
          + "{:^{w}}".format(text1, w=between_space - 2)
          + "{:<{w}}".format(border, w=box_size + 1)
          + "{:^{w}}".format("", w=between_space - 1)
          + "{:>{w}}".format(border, w=box_size + 2)
          + "{:^{w}}".format(text2, w=between_space - 2)
          + "{:<{w}}".format(border, w=end_space // 2 + 2)
          + border)

    print(border
          + "{:^{w}}".format(border * begin_space, w=box_size)
          + "{:^{w}}".format("", w=2 * box_size - 1)
          + "{:^{w}}".format(border * begin_space, w=box_size)
          + border)


def print_button(text1, border='#'):
    print(border
          + "{:^{w}}".format(border * begin_space, w=box_size)
          + "{:^{w}}".format("", w=2 * box_size - 1)
          + "{:^{w}}".format("", w=box_size)
          + border)

    print(border
          + "{:>{w}}".format(border, w=begin_space // 2 + 2)
          + "{:^{w}}".format(text1, w=between_space - 2)
          + "{:<{w}}".format(border, w=box_size + 1)
          + "{:^{w}}".format("", w=between_space - 1)
          + "{:>{w}}".format("", w=box_size + 2)
          + "{:^{w}}".format("", w=between_space - 2)
          + "{:<{w}}".format("", w=end_space // 2 + 2)
          + border)

    print(border
          + "{:^{w}}".format(border * begin_space, w=box_size)
          + "{:^{w}}".format("", w=2 * box_size - 1)
          + "{:^{w}}".format("", w=box_size)
          + border)


def print_one_button(text1, border='#'):
    print(border
          + "{:^{w}}".format('#' * (terminal_width // 2), w=terminal_width - 2)
          + border)

    print(border
          + "{:>{w}}".format("#", w=terminal_width // 4)
          + "{:^{w}}".format(text1, w=terminal_width // 2 - 2)
          + "{:<{w}}".format("#", w=terminal_width // 4 + 1)
          + border)

    print(border
          + "{:^{w}}".format('#' * (terminal_width // 2), w=terminal_width - 2)
          + border)


def print_table_row(apartments, number, total, border='#'):
    print(border
          + "{:^{w}}".format(str(apartments[0][number]['number']) + '.', w=box_size // 2)
          + border
          + "{:^{w}}".format(apartments[0][number]['utilities']['electricity'], w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format(apartments[0][number]['utilities']['gas'], w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format(apartments[0][number]['security']['monitoring'], w=box_size // 2)
          + border
          + "{:^{w}}".format(apartments[0][number]['security']['guard'], w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format(apartments[0][number]['building']['cleaning'], w=box_size // 2)
          + border
          + "{:^{w}}".format(apartments[0][number]['building']['maintenance'], w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format(total, w=box_size // 2)
          + border)


def print_table_header(border="#"):
    print_border()
    print(border
          + "{:^{w}}".format('Type', w=box_size // 2)
          + border
          + "{:^{w}}".format('Utilities', w=box_size - 2)
          + border
          + "{:^{w}}".format('Security', w=box_size - 1)
          + border
          + "{:^{w}}".format('Building', w=box_size - 1)
          + border
          + "{:^{w}}".format('', w=box_size // 2)
          + border)
    print_border()
    print(border
          + "{:^{w}}".format("Nr./ Subtype", w=box_size // 2)
          + border
          + "{:^{w}}".format("Electricity", w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format("Gas", w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format("Monitoring", w=box_size // 2)
          + border
          + "{:^{w}}".format("Guard", w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format("Cleaning", w=box_size // 2)
          + border
          + "{:^{w}}".format("Maintenance", w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format("Total", w=box_size // 2)
          + border)
    print_border()


def print_expenses_header(border='#'):
    print_border()
    print(border
          + "{:^{w}}".format('Nr.', w=box_size)
          + border
          + "{:^{w}}".format('Type', w=box_size)
          + border
          + "{:^{w}}".format('Subtype', w=box_size - 2)
          + border
          + "{:^{w}}".format('Amount', w=box_size - 2)
          + border)
    print_border()


def print_expenses_table(apartments, number, type, subtype, border='#'):
    print(border
          + "{:^{w}}".format(str(apartments[0][number - 1]['number']) + '.', w=box_size)
          + border
          + "{:^{w}}".format(type, w=box_size)
          + border
          + "{:^{w}}".format(subtype, w=box_size - 2)
          + border
          + "{:^{w}}".format(apartments[0][number - 1][type][subtype], w=box_size - 2)
          + border)
    print_border()


def print_search_table_header(date, sum, border='#'):
    print_border()
    print(border
          + "{:^{w}}".format('Date', w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format('Nr.', w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format('Type', w=box_size)
          + border
          + "{:^{w}}".format('Subtype', w=box_size - 2)
          + border
          + "{:^{w}}".format('Amount', w=box_size - 2)
          + border)
    print_border()


def print_search_table_row(data, number, type, subtype, amount, border='#'):
    print(border
          + "{:^{w}}".format(data, w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format(number, w=box_size // 2 - 1)
          + border
          + "{:^{w}}".format(type, w=box_size)
          + border
          + "{:^{w}}".format(subtype, w=box_size - 2)
          + border
          + "{:^{w}}".format(amount, w=box_size - 2)
          + border)
    print_border()
