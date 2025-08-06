"""
Project management
Estimate: 30 minutes
Actual:   182 minutes
"""
# TODO: Functions:
#   load_projects (complete)
#   save_projects (complete)
#   display_projects (complete)
#   filter_projects (complete)
#   add_project (complete)
#   update_project (complete)

from datetime import datetime
from project import Project

FILENAME = "projects.txt"

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)

    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load: ") + ".txt"
            try:
                projects = load_projects(filename)
            except (FileNotFoundError, ValueError):  #Error handling for invalid file
                print(f"Failed to load from {filename} check the file and try again.")
        elif choice == 's':
            filename = input(f"Enter filename to save:") + ".txt"
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            confirm = input(f"Would you like to save to {FILENAME}? ").lower()
            if confirm in ['yes', 'y']:
                save_projects(FILENAME, projects)

            """ # Good alternative doesn't match sample
            else:
                filename = input(f"Enter filename to save:") + ".txt"
                save_projects(filename,projects)
            """
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option")

def load_projects(filename):
    """Load projects from file and returns a list"""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name, start_str, priority, cost, completion = parts
            start_date = datetime.strptime(start_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    """Save projects to file"""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                       f"\t{project.cost:.2f}\t{project.completion}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    """Display projects grouped by completion status."""
    print("Incomplete projects:")
    for p in sorted([p for p in projects if p.completion < 100], key=lambda x: x.priority):
        print(f"  {p}")
    print("Completed projects:")
    for p in sorted([p for p in projects if p.completion == 100], key=lambda x: x.priority):
        print(f"  {p}")

def filter_projects(projects):
    """Filter projects after specified date"""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        date = datetime.strptime(date_str, "%d/%m/%y").date()
        for p in sorted([p for p in projects if p.start_date >= date], key=lambda x: x.start_date):
            print(p)
    except ValueError:
        print("Invalid date format. Please enter as dd/mm/yy.")  # Added error handling

def add_project(projects):
    """Adds new project to projects list"""
    print("Let's add a new project")
    name = input("Name: ")
    start_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(start_str, "%d/%m/%y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))

def update_project(projects):
    """Updates existing project in projects list"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        index = int(input("Project choice: "))
        if not 0 <= index < len(projects):
            print("Invalid project index.")
            return
        project = projects[index]
        print(project)
        new_completion = input("New Percentage: ")
        if new_completion:
            project.completion = int(new_completion)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except ValueError:
        print("Invalid input. Enter valid option.")

if __name__ == '__main__':
    main()

