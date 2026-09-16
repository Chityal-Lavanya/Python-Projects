import json

FILE_NAME = "8_Student_Management_System/students.json"

class Student:

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    # Convert object into dictionary
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

    # Display student details
    def display(self):
        print("-" * 35)
        print(f"ID     : {self.student_id}")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print("-" * 35)

class StudentManagementSystem:

    def __init__(self):
        self.students = []
        self.load_students()

    # CREATE
    def add_student(self):

        student_id = input("Enter student ID: ").strip()

        # Check duplicate ID
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter student name: ").strip()

        try:
            age = int(input("Enter student age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                return

        except ValueError:
            print("Invalid age! Please enter a number.")
            return

        course = input("Enter course: ").strip()

        student = Student(
            student_id,
            name,
            age,
            course
        )

        self.students.append(student)

        self.save_students()

        print("Student added successfully!")

    # READ
    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        print("\n===== STUDENT LIST =====")

        for student in self.students:
            student.display()

    # SEARCH
    def search_student(self):

        keyword = input(
            "Enter student ID or name: "
        ).strip().lower()

        found = False

        for student in self.students:

            if (
                keyword in student.student_id.lower()
                or keyword in student.name.lower()
            ):
                student.display()
                found = True

        if not found:
            print("Student not found.")

    # UPDATE
    def update_student(self):

        student_id = input(
            "Enter student ID to update: "
        ).strip()

        for student in self.students:

            if student.student_id == student_id:

                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Course")
                print("4. Update All")

                choice = input(
                    "Enter your choice: "
                ).strip()

                if choice == "1":

                    student.name = input(
                        "Enter new name: "
                    ).strip()

                elif choice == "2":

                    try:
                        new_age = int(
                            input("Enter new age: ")
                        )

                        if new_age <= 0:
                            print("Invalid age.")
                            return

                        student.age = new_age

                    except ValueError:
                        print("Invalid age.")
                        return

                elif choice == "3":

                    student.course = input(
                        "Enter new course: "
                    ).strip()

                elif choice == "4":

                    student.name = input(
                        "Enter new name: "
                    ).strip()

                    try:
                        student.age = int(
                            input("Enter new age: ")
                        )

                        if student.age <= 0:
                            print("Invalid age.")
                            return

                    except ValueError:
                        print("Invalid age.")
                        return

                    student.course = input(
                        "Enter new course: "
                    ).strip()

                else:
                    print("Invalid choice.")
                    return

                self.save_students()

                print("Student updated successfully!")
                return

        print("Student not found.")

    # DELETE
    def delete_student(self):

        student_id = input(
            "Enter student ID to delete: "
        ).strip()

        for student in self.students:

            if student.student_id == student_id:

                self.students.remove(student)

                self.save_students()

                print("Student deleted successfully!")
                return

        print("Student not found.")

    # SAVE TO FILE
    def save_students(self):

        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    # LOAD FROM FILE
    def load_students(self):

        try:

            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            for item in data:

                student = Student(
                    item["student_id"],
                    item["name"],
                    item["age"],
                    item["course"]
                )

                self.students.append(student)

        except FileNotFoundError:
            self.students = []

        except json.JSONDecodeError:
            print("Student file is empty or corrupted.")
            self.students = []

# Main Program
system = StudentManagementSystem()


while True:

    print("\n--------------------------------")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("----------------------------------")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input(
        "\nEnter your choice: "
    ).strip()

    if choice == "1":

        system.add_student()

    elif choice == "2":

        system.view_students()

    elif choice == "3":

        system.search_student()

    elif choice == "4":

        system.update_student()

    elif choice == "5":

        system.delete_student()

    elif choice == "6":

        print("Student data saved. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-6.")