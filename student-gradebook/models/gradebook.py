class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.id] = student
        print(f"Student {student.name} added successfully")
        return student

    def get_student(self, id):
        if id in self.students:
            return self.students[id]
        else:
            print(f"Student not found with id #{id}")
            return None
        
    def remove_student(self, id):
        if id in self.students:
            remove_index = self.students.pop(id)
            print(f"Student {remove_index.name} removed successfully")
            return remove_index
        else:
            print(f"Student not found with id #{id}")
            return None

    def print_report_cards(self):
        if not self.students:
            print("Student list is empty")
        else:
            for student in self.students.values():
                print(f"Student: {student.name}")

                for entry in student.grades:
                    print(f"    {entry.course.name}: {entry.grade:,.2f}")

                print(f"    GPA: {student.calculate_gpa()}")
                print("-" * 20)

    def __str__(self):
        return f"GradeBook with {len(self.students)} students"
