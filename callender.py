import calendar

def display_calendar(year, month):
    print(calendar.month(year, month))
reminders = {}  # e.g., {'2025-05-24': ['Doctor Appointment at 10 AM']}
def add_reminder(date, reminder):
    if date in reminders:
        reminders[date].append(reminder)
    else:
        reminders[date] = [reminder]

def view_reminders(date):
    return reminders.get(date, [])

def delete_reminder(date, reminder):
    if date in reminders:
        reminders[date].remove(reminder)
        if not reminders[date]:
            del reminders[date]
def main():
    while True:
        print("\nCalendar and Reminder App")
        print("1. Show Calendar")
        print("2. Add Reminder")
        print("3. View Reminders")
        print("4. Delete Reminder")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))
            display_calendar(year, month)
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            reminder = input("Enter reminder: ")
            add_reminder(date, reminder)
            print("Reminder added.")
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            r = view_reminders(date)
            if r:
                print("Reminders:", r)
            else:
                print("No reminders for this date.")
        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD): ")
            reminder = input("Enter reminder to delete: ")
            delete_reminder(date, reminder)
            print("Reminder deleted.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()
