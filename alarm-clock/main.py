from models import Clock

def alarm_clock():
    clock = Clock()
    clock.add_alarm()
    clock.check_alarm()

def main():
    try:
        alarm_clock()
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    return 0

if __name__ == '__main__':
    main()