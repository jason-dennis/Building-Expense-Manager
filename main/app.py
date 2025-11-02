"""
Create an app to manage monthly expenses for apartments in a block of flats.
This application stores expenses for each apartment: the amount and the type of expenses.
Expenses are:
- Utilities : electricity, gas
- Security :  monitoring, guard
- Building : cleaning,maintenance

Suppose that the building has 4 floors and 5 apartments on each floor

Floor 1: 1,2,3,4,5
Floor 2: 6,7,8,9,10
Floor 3: 11,12,13,14,15
Floor 4: 16,17,18,19,20

apartments={
    "floor": int
    "number": int
    "utilities": {"electricity": int, "gas": int}
    "security: {"monitoring": int, "guard": int}
    "building": {"cleaning": int, "maintenance": int}
}
utilities={
    "YYYY/MM/DD": { "type" {"subtype": int},"number":int}
}
"""
from collections import defaultdict

import tests.Test_functions as Test
import Service.program as Program
import Service.functionalities as Func


def main():
    """
        This function run the entire application.
    """
    Test.test()
    utilities = [defaultdict(list), []]
    apartments = Func.create_apartments()
    Program.run_app(apartments, utilities)


if __name__ == "__main__":
    main()
