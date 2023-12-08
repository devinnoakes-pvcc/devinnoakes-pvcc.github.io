# Name: Devin Noakes
# Prog Purpose: This program creates a payroll report


import datetime

# LISTS of data
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
       "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M"]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

# new lists for calculated amounts
gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []  # Added this line
medicare = []  # Added this line
net_pay = []  # Added this line

total_gross = 0
total_net = 0

# tuples of constants
PAY_RATE = (16.50, 15.75, 19.50)
DED_RATE = (0.12, 0.03, 0.062, 0.0145, 0.04)

# define program
def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total_gross, total_net, gross_pay, fed_tax, state_tax, soc_sec, medicare, net_pay

    for i in range(num_emps):
        # calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[2]  # Adjusted index to match tuple length

        # calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]

        # calculate other deductions and NET PAY here
        net = pay - fed - state  # Adjusted deduction calculation

        # add to totals
        total_gross += pay
        total_net += net

        # append amounts to list
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(0)  # You need to replace 0 with the actual calculation for Social Security
        medicare.append(0)  # You need to replace 0 with the actual calculation for Medicare
        net_pay.append(net)

def display_results():
    currency = '${:,.2f}'.format
    line = '--------------------------------'
    tab = "\t"

    print(line)
    print('******************** FRESH FOODS MARKET ************************')
    print(line)
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "Emp  Name" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
    print(titles1 + titles2)

    # print employee data
    for i in range(num_emps):
        data1 = f"{emp[i]}{tab}{job[i]}{tab}{currency(gross_pay[i])}{tab}"  # Adjusted formatting
        data2 = f"{currency(fed_tax[i])}{tab}{currency(state_tax[i])}{tab}"  # Adjusted formatting
        data3 = f"{currency(soc_sec[i])}{tab}{currency(medicare[i])}{tab}{currency(net_pay[i])}"  # Adjusted formatting
        print(data1 + data2 + data3)

    print(line)
    print("******************** TOTAL GROSS: " + currency(total_gross))
    print("******************** TOTAL NET :  " + currency(total_net))

# call the main program to execute
main()
