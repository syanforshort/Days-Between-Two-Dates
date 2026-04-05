from datetime import datetime

# Function for the whole thing
def calc_days():
    print("--- Date Duration Calculator ---")
    print("Enter dates in YYYY-MM-DD format (e.g., 2000-01-01) and Today for present date!")

    today = datetime.now()

    try:
        # Convert strings into datetime objects
        # %Y = 4-digit year, %m = month, %d = day
        date_format = '%Y-%m-%d'

        # Handle start date
        start_input = input("Enter the start date: ").strip().lower()
        if start_input == 'today':
            start_date = today
        else:
            start_date = datetime.strptime(start_input, date_format) 

        # Handle end date
        end_input = input("Enter the end date: ")
        if end_input == 'today':
            end_date = today
        else:
            end_date = datetime.strptime(end_input, date_format)


        # Calculate the difference
        delta = end_date - start_date

        # Display the result
        # Using abs() for later dates being put first
        print(f"\nTotal difference: {abs(delta.days)} days")

        # Loop for repetitive use
        while True:
            repeat = input("Do you want to calculate again? (Y / N)").strip().lower()

            if repeat == 'y':
                calc_days()

            else:
                print("Thank you for using this date calculator!")
                break


    except ValueError:
        print("\nError. Please use the specified format (YYYY-MM-DD) or the word 'Today'.")
        calc_days()

if __name__ == "__main__":
    calc_days()

