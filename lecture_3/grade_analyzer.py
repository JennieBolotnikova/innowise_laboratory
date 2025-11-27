"""
The student grade analyzer
A single console-based program that manages and analyze the students grades
"""

#add a new student to the students list
def add_student(students):
    name = input("Enter student name: ")
    # Validate that name is not empty
    if not name:
        print("Name cannot be empty!")
        return
    # Check if student already exists
    for s in students:
        if s["name"] == name:
            print("Student with this name already exist")
            return
    # Create new student dictionary and add to the students list
    student = {"name": name, "grades": []}
    students.append(student)

#Add grades for a student
def add_grade(students):
    # Check if there are any students in the list
    if not students:
        print("No student found. Please add a student first.")
        return

    name = input("Enter student name: ")
    student = None
    # Search for student by name
    for s in students:
        if s['name'].lower() == name.lower():
            student = s
            break

    if student is None:
        print(f"Student {name} not found")
        return
    #Continuous grade input until user types 'done'
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ")
        if grade_input == "done":
            break
        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")

#Show report for all students
def show_report(students):
    print("---Students report---")
    # Check if there are any students in the list
    if not students:
        print("No student found")
        return

    student_averages = []
    all_grades = []
    # Calculate averages for each student
    for s in students:
        grades = s.get("grades", [])
        if len(grades) != 0:
            try:
                average = sum(grades) / len(grades)
                print(f"{s['name']}'s average grade is {average}")
                student_averages.append(average)
                all_grades.extend(grades)
            except ZeroDivisionError:
                print(f"{s['name']}'s average grade is N/A")
        else:
            print(f"{s['name']}'s average grade is N/A")



    if not student_averages:
        print("No grades has been found")
    else:
        overall_average = sum(all_grades) / len(all_grades)
        max_average = max(student_averages)
        min_average = min(student_averages)
        print("----------")
        print(f"Max average: {max_average}")
        print(f"Min average: {min_average}")
        print(f"Overall average: {overall_average}")

#Find the student with the highest average grades
def find_top_performer(students):
    # Check if there are any students in the list
    if not students:
        print("No students added")
        return
    # Find student with maximum average grade
    try:
        top_performer = max(students, key = lambda s: sum(s["grades"]) / len(s["grades"]) if s.get("grades") else 0)
        top_performer_name = top_performer["name"]
        max_avg = sum(top_performer["grades"]) / len(top_performer["grades"])
        if not top_performer_name:
            print("No students added")
        elif not top_performer.get("grades"):
            print("No grades added")
        else:
            print(f"The student with a highest average is {top_performer_name} with a grade of {max_avg}")
    except KeyError as e:
        print(f"Missing required field: {e}")
    except ZeroDivisionError:
        print("No grades added")


#Main menu loop for the Student Grade Analyzer
def menu(students):
    while True:
        print("1. Add a nex student")
        print("2. Add a grade for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            add_student(students)
        elif choice == 2:
            add_grade(students)
        elif choice == 3:
            show_report(students)
        elif choice == 4:
            find_top_performer(students)
        elif choice == 5:
            break
        else:
            print("Invalid menu item. Please enter a number between 1-5.")

# Initialize empty students list and start application
if __name__ == '__main__':
    students = []
    menu(students)