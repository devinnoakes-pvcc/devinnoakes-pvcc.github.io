from datetime import datetime

def calculate_tax(assessed_value, is_eligible_for_relief):
    # Constants
    annual_tax_rate = 4.20 / 100  # 4.20% per year
    relief_rate = 0.33  # 33% relief for qualified vehicles

    # Calculate annual tax amount
    annual_tax_amount = assessed_value * annual_tax_rate

    # Calculate six-month tax bill
    six_month_bill = annual_tax_amount / 2

    # Calculate relief amount if eligible
    relief_amount = 0
    if is_eligible_for_relief:
        relief_amount = six_month_bill * relief_rate

    # Calculate total due
    total_due = six_month_bill - relief_amount

    return six_month_bill, relief_amount, total_due

def print_tax_bill(assessed_value, six_month_bill, relief_amount, total_due):
    # Print tax bill
    print("\nPersonal Property Tax Bill")
    print("Date/Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Assessed Value: ${:,.2f}".format(assessed_value))
    print("Full Annual Amount Owed: ${:,.2f}".format(six_month_bill * 2))
    print("Relief Amount: ${:,.2f}".format(relief_amount))
    print("Total Due: ${:,.2f}".format(total_due))

# Input loop
while True:
    try:
        # Get user input
        assessed_value = float(input("Enter the assessed value of the vehicle: $"))
        eligible_for_relief = input("Is the vehicle eligible for tax relief? (Y/N): ").upper() == 'Y'

        # Calculate tax
        six_month_bill, relief_amount, total_due = calculate_tax(assessed_value, eligible_for_relief)

        # Print tax bill
        print_tax_bill(assessed_value, six_month_bill, relief_amount, total_due)

        # Ask if the user wants to calculate for another vehicle
        another_vehicle = input("\nDo you want to calculate tax for another vehicle? (Y/N): ").upper()
        if another_vehicle != 'Y':
            break  # Exit the loop if the user doesn't want to calculate for another vehicle

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the assessed value.")
