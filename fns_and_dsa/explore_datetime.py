# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # save current date in variable
    current_date = datetime.now()
    # format to "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date, days):
    # calculate future date
    future_date = current_date + timedelta(days=days)
    # format to "YYYY-MM-DD"
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date

def main():
    # part 1
    current_date = display_current_datetime()

    # part 2
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days_to_add)

if __name__ == "__main__":
    main()