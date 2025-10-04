class GradeEntry:
    def __init__(self, course, grade):
        self.course = course
        self.grade = grade

    def __str__(self):
        return f"{self.course.name}: {self.grade:,.2f}"