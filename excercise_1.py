# Tasks
# EXERCISE 1
# Age Calculator

# Import datetime class to convert string input into date
# Import date class to get today's date
from datetime import datetime, date

try:
    # Ask the user to enter date of birth in mm/dd/yyyy format
    birth_input = input("Enter your date of birth (mm/dd/yyyy): ").strip()

    # Convert the entered string into a date object using specified format
    birth_date = datetime.strptime(birth_input, "%m/%d/%Y").date()

    # Get today's current date
    today = date.today()

    # Check if the birth date is in the future
    if birth_date > today:
        raise ValueError("Birth date cannot be in the future.")

    # Calculate initial age by subtracting years
    age = today.year - birth_date.year

    # Adjust age if birthday has not occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    # Convert birth date into European format (dd/mm/yyyy)
    european_format = birth_date.strftime("%d/%m/%Y")

    # Display the results
    print("\n---- AGE CALCULATOR RESULTS ----")
    print(f"Your age is: {age} years")
    print(f"Birth date (European format): {european_format}")

# Handle incorrect date format or invalid date
except ValueError:
    print("Please enter a valid date in mm/dd/yyyy format.")

# Handle any unexpected errors
except Exception as ex:
    print("Error:", ex)
    print("An unexpected error occurred. Please try again.")



