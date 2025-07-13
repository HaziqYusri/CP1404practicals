"""
Project management
Estimate: 30 minutes
Actual:    minutes
"""
# TODO: Functions:
#   load_projects (ongoing)
#   save_projects (incomplete)
#   display_projects (incomplete)
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
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'l':
            break
        elif choice == 's':
            #save_projects(filename, projects)
            break
        elif choice == 'd':
            #display_projects(projects)
            break
        elif choice == 'f':
            #filter_projects(projects)
            break
        elif choice == 'a':
            #add_project(projects)
            break
        elif choice == 'u':
            #update_project(projects)
            break
        elif choice == 'q':
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
    return projects



if __name__ == '__main__':
    main()

