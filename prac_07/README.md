# Practical 07
## Overview
This practical contains two main tasks:
1. **Guitars Program (Guitars 2.0)** – Refactor previous guitar code to read from and write to a CSV file, using a `Guitar` class.
2. **Project Management Program** – Develop a program to manage a list of projects using a `Project` class and a simple text menu interface.

---

## Task 1: More Guitars

### Description
The program reads a list of guitars from a `.csv` file and allows the user to view, add, and save guitars.

### Key Features
- Load guitar data from `guitars.csv`
- Display formatted output with alignment and vintage tagging
- Add new guitars via user input
- Save the full updated list back to the CSV file

### Files
- `guitar.py`: Defines the `Guitar` class
- `guitars.py`: Main program that uses the class and provides the interface
- `guitars.csv`: Input/output CSV data file

---

## Task 2: Project Management Program

### Description
This task focuses on working with a list of project records stored in a text file. The program allows updating  and saving projects using a `Project` class.

### Key Features
- Load projects from `projects.txt`
- Display incomplete and complete projects
- Filter projects by start date
- Add new projects
- Update selected projects
- Save changes back to `projects.txt`

### Files
- `project.py`: Defines the `Project` class
- `project_management.py`: Console program with a menu interface for managing projects
- `projects.txt`: Data file storing projects

---

### Lessons on "Clean Code"
- Avoid repetition using loops and list comprehensions
- Use constants (like `CURRENT_YEAR`) where needed
- Meaningful function names and clear separation of concerns
- Single Responsibility Principle (each function does one thing)
