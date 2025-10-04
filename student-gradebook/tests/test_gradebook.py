import unittest
import sys
import os
from models import Course, GradeEntry, Student, GradeBook

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestGradeBook(unittest.TestCase):
    def test_add_student(self):
        course = Course("MATH001", "Mathematics")
        grade = 95
        student = Student("STU001", "John Doe")
        student.add_grade(GradeEntry(course, grade))
        self.assertEqual(len(student.grades), 1)
        self.assertEqual(student.grades[0].course, course)
        self.assertEqual(student.grades[0].grade, grade)
        
        gb = GradeBook()
        gb.add_student(student)
        self.assertEqual(len(gb.students), 1)
        self.assertEqual(gb.students[student.id], student)

        student2 = Student("STU002", "Jane Doe")
        gb.add_student(student2)
        self.assertEqual(len(gb.students), 2)
        self.assertEqual(gb.students[student2.id], student2)

        student3 = Student("STU003", "Bob Smith")
        gb.add_student(student3)
        self.assertEqual(len(gb.students), 3)
        self.assertEqual(gb.students[student3.id], student3)

    def test_remove_student(self):
        course = Course("MATH001", "Mathematics")
        grade = 95
        student = Student("STU001", "John Doe")
        student.add_grade(GradeEntry(course, grade))
        self.assertEqual(len(student.grades), 1)
        self.assertEqual(student.grades[0].course, course)
        self.assertEqual(student.grades[0].grade, grade)
        
        gb = GradeBook()
        gb.add_student(student)
        self.assertEqual(len(gb.students), 1)
        self.assertEqual(gb.students[student.id], student)

        gb.remove_student(student.id)
        self.assertEqual(len(gb.students), 0)

if __name__ == "__main__":
    unittest.main()