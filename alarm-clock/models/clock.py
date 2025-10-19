from .alarm import Alarm
import time
import winsound

class Clock(Alarm):
    def add_alarm(self):
        print("Enter alarm times in 24-hour format. Type 'done' when finished.")

        while True:
            user_input = input("Set alarm (HH:MM:SS): ").strip()
            if user_input.lower() == 'done':
                print(f"\nTotal {len(self.alarms)} alarms set on: {", ".join(self.alarms)}")
                break
            try:
                alarm_time = time.strptime(user_input, "%H:%M:%S")
                formatted_time = time.strftime("%H:%M:%S", alarm_time)
                if formatted_time not in self.alarms:
                    self.alarms.append(formatted_time)
                    print(f"Alarm set on: {formatted_time}")
                else:
                    print(f"Alarm already set at: {formatted_time}")
            except ValueError:
                print("Invalid format. Please enter time as HH:MM:SS")

    def check_alarm(self):
        if not self.alarms:
            print("\nNo alarm set.")
            return
        print("\nAlarm checking started...")
        try:
            while True:
                now = time.strftime("%H:%M:%S", time.localtime())
                if now in self.alarms and now not in self.triggered_alarms:
                    self.ring_alarm(now)
                    self.triggered_alarms.add(now)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nAlarm clock stopped!")

    def ring_alarm(self, alarm_time):
        print(f"\n{'Ring! ' * 5}")
        print(f"Alarm time is: {alarm_time}")
        winsound.Beep(1000, 1000)