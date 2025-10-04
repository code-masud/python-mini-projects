class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []

    def add_grade(self, grate_entry):
        self.grades.append(grate_entry)
        print(f"Grade for {grate_entry.course.name} added successfully to {self.name}")

    def calculate_gpa(self):
        if not self.grades:
            return 0
        else:
            total = sum(entry.grade for entry in self.grades)
            return round(total / len(self.grades), 2)

    def __str__(self):
        return f"Student: {self.name}"