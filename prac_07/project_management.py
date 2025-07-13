"""
Project management
Estimate: 30 minutes
Actual:    minutes
"""
# TODO: Functions:
#   load_projects (ongoing)
#   save_projects (ongoing)
#   display_projects (ongoing)
#   filter_projects (incomplete)
#   add_project (incomplete)
#   update_project (incomplete)

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
            projects = load_projects(filename)
        elif choice == 's':
            filename = input(f"Enter filename to save:") + ".txt"
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects(projects)
        elif choice == 'a':
            #add_project(projects)
            break
        elif choice == 'u':
            #update_project(projects)
            break
        elif choice == 'q':
            confirm = input(f"Would you like to save to {FILENAME}? ").lower()
            if confirm in ['yes', 'y']:
                save_projects(FILENAME, projects)
            else:
                filename = input(f"Enter filename to save:") + ".txt"
                save_projects(filename,projects)
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
    date = datetime.strptime(date_str, "%d/%m/%y").date()
    for p in sorted([p for p in projects if p.start_date >= date], key=lambda x: x.start_date):
        print(p)

if __name__ == '__main__':
    main()

