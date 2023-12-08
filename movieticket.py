# Name:Devin Noakes
# Prog Purpose: This program finds the cost of movie tickets.
#   Price for ticket: $10.99
#   Price for drink : $4.99
#   price for popcorn: 8.99
#   Sales tax rate: 5.5%

import datetime

# Define global variables
SALES_TAX_RATE = 0.055
PR_TICKET = 10.99
PR_DRINK = 4.99
PR_POPCORN = 8.99

num_ticket = 0
ticket_cost = 0
num_drink = 0
drink_cost = 0
num_popcorn = 0
popcorn_cost = 0
sales_tax = 0
subtotal = 0
total = 0

def main():
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again? (Y or N): ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO":
            more = False
            print("Thank you for your order. Enjoy your movie!")

def get_user_data():
    global num_ticket, num_popcorn, num_drink
    num_ticket = int(input("Number of tickets: "))
    num_popcorn = int(input("Number of popcorns: "))
    num_drink = int(input("Number of drinks: "))

def perform_calculations():
    global subtotal, sales_tax, total, ticket_cost, popcorn_cost, drink_cost
    ticket_cost = num_ticket * PR_TICKET
    popcorn_cost = num_popcorn * PR_POPCORN
    drink_cost = num_drink * PR_DRINK
    subtotal = ticket_cost + popcorn_cost + drink_cost
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    money_format = '${:,.2f}'
    line = '------------------------------'
    print(line)
    print('**** CINEMA HOUSE MOVIES ****')
    print('--- Your neighborhood MOVIE HOUSE ---')
    print(line)
    print('Ticket       ' + money_format.format(PR_TICKET) + ' x ' + str(num_ticket) + '  $ ' + money_format.format(ticket_cost))
    print('Drink        ' + money_format.format(PR_DRINK) + ' x ' + str(num_drink) + '  $ ' + money_format.format(drink_cost))
    print(line)
    print('Subtotal                    $ ' + money_format.format(subtotal))
    print('Popcorn      ' + money_format.format(PR_POPCORN) + ' x ' + str(num_popcorn) + '  $ ' + money_format.format(popcorn_cost))
    print('Sales Tax                   $ ' + money_format.format(sales_tax))
    print('Total                       $ ' + money_format.format(total))
    print()
    print(str(datetime.datetime.now()))

# Call the main program to execute
main()
