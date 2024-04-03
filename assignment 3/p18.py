#Write a program which takes the month number as an input and display number of days in that month.
def get_days_in_month(month):
    # Dictionary mapping month number to days
    days_in_month = {
        1: 31,
        2: 28,  # Assuming non-leap year
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # Check if month is valid
    if month in days_in_month:
        return days_in_month[month]
    else:
        return "Invalid month number. Please enter a number between 1 and 12."

# Get input from user
month_number = int(input("Enter the month number (1-12): "))

# Get and print the number of days in the specified month
print(f"Number of days in month {month_number}: {get_days_in_month(month_number)}")