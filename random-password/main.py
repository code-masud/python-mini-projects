from models import Password

def demonstrate_function():
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Length must be integer")
    except Exception as e:
        print(f"An error occurred while input length: {e}")
    else:
        password = Password(length)
        result = password.generate()
        print(f"Your password: {result}")

def main():
    try:
        demonstrate_function()
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        return 0
    return 1

if __name__ == '__main__':
    exit(main())