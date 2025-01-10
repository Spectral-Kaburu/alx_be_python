from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    print(f"current date and time: {current_date}")

def calculate_future_date():
    days = input("Enter the number of days to add to the current date: ")
    future_date = datetime.now() + datetime.timedelta(days=days)
    print(f"Future date : {future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
