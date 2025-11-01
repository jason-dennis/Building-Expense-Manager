# Building-Expense-Manager
Building Expense Manager is a Python-based application designed to efficiently manage building-related expenses for multiple apartments. It was developed as part of a university coursework project and represents my first complete project in Python.
The application provides a command-line interface (CLI) that allows users to record, modify, filter, and analyze expenses. It emphasizes modular design, data validation, and command-driven interaction.

🎯 Objectives
The primary goal of this project was to strengthen core Python programming and software engineering skills, focusing on:
    Working with lists and dictionaries for data management
    Implementing a modular architecture
    Managing data operations and user input through a text-based interface
    Applying principles of clean and maintainable code
    Following Feature-Driven Development (FDD) and Test-Driven Development (TDD) methodologies to ensure structured, iterative implementation and reliable testing

⚙️ Key Features
    1. Add
        Add a new expense entry for a specific apartment
        Modify an existing expense
    2. Delete
        Remove all expenses associated with a specific apartment
        Remove expenses for a range of consecutive apartments
        (e.g., if apartments 2 and 5 are provided, expenses for apartments 2–5 are deleted)
        Remove all expenses of a specific type across all apartments
    3. Search
        Display all apartments with total expenses greater than a specified amount
        Display all expenses of a given type across all apartments
        Display all expenses made before a specific date and greater than a specified amount
    4. Reports
        Calculate and display the total sum for a given type of expense
        Display all apartments sorted by a specific expense type
        Display the total expenses for a selected apartment
    5. Filter
        Filter out all expenses of a certain type
        Filter out all expenses below a specified amount
    6. Undo
        Revert the most recent operation, restoring the expense list to its previous state

🧰 Technologies
    Python 3
    Command-Line Interface (CLI)
    Feature-Driven Development (FDD)
    Test-Driven Development (TDD)
