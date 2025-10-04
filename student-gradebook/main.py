from models import Course, GradeEntry, Student, GradeBook

def demonstrate_functions():
    print("\n --- Student Gradebook ---")
    math = Course("MATH001", "Mathematics")
    eng = Course("ENG002", "English")

    s1 = Student(1, "Bob")
    s2 = Student(2, "John")

    s1.add_grade(GradeEntry(math, 95))
    s1.add_grade(GradeEntry(eng, 80))

    s2.add_grade(GradeEntry(math, 75))
    s2.add_grade(GradeEntry(eng, 65))

    gb = GradeBook()
    gb.add_student(s1)
    gb.add_student(s2)

    print("\n--- Initial Report Cards ---")
    gb.print_report_cards()

    print("\n--- Operations ---")
    gb.remove_student(2)

    print("\n--- Final Report Cards ---")
    gb.print_report_cards()

def main():
    try:
        demonstrate_functions()
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
