"""
Project management
Estimate: 30 minutes
Actual:    minutes
"""
# TODO: Functions:
#   load_projects
#   save_projects
#   display_projects
#   filter_projects
#   add_project
#   update_project

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
    print(f"Loaded {len(projects)} projects from {FILENAME}")

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
    return projects

if __name__ == '__main__':
    main()

