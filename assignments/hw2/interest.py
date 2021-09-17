"""
Name: Reginald Wigfall
interest.py

Problem: calculate the monthly interest charge on a credit card account
Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    rate = eval(input("input annual interest rate: "))  # input account's annual interest
    days = eval(input("input number of days in billing cycle: "))  # input days in billing cycle
    previous_balance = eval(input("input the net balance: "))  # input net balance
    payment = eval(input("input the payment amount: "))  # input payment amount
    payment_day = eval(input("input day of payment in billing cycle"))  # input day of payment
    average_daily = ((previous_balance * days) - (payment * (days - payment_day))) / days
    monthly_interest = round(average_daily * ((rate / 12) / 100), 2)
    print(monthly_interest)  # print the monthly interest charge


if __name__ == '__main__':
    main()
