task = input("Enter your task: ")
priority = input("(high/medium/low)").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time == "no":
            print(f"'{task}' is a high priority task that must be done at your earliest convinience.")
        else:
            print(f"'{task}' is a high priority task that requires your immediate attention today!")
    case "medium":
        if time == "no":
            print(f"'{task}' is a medium priority task that should be done at your earliest convinience.")
        else:
            print(f"'{task}' is a medium priority task that requires your immediate attention today!")
    case "low":
        if time == "no":
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"'{task}' is a low priority task. Consider doing it right now!")