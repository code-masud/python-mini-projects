import unittest
import sys
import os
from models import Course, GradeEntry, Student

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("STU001", "John Doe")
        self.assertEqual(student.id, "STU001")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.grades, [])

    def test_add_grade(self):
        course = Course("MATH001", "Mathematics")
        grade = 95
        student = Student("STU001", "John Doe")
        student.add_grade(GradeEntry(course, grade))
        self.assertEqual(len(student.grades), 1)
        self.assertEqual(student.grades[0].course, course)
        self.assertEqual(student.grades[0].grade, grade)

    def test_calculate_gpa(self):
        student = Student("STU001", "John Doe")
        course1 = Course("MATH001", "Mathematics")
        course2 = Course("ENG002", "English")
        grade1 = 95
        grade2 = 80
        student.add_grade(GradeEntry(course1, grade1))
        student.add_grade(GradeEntry(course2, grade2))
        self.assertEqual(student.calculate_gpa(), (grade1 + grade2) / 2)

if __name__ == "__main__":
    unittest.main()