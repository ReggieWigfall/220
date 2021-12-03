"""
Name: Reginald Wigfall
sales_person.py

Problem: Write a class of data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


class SalesPerson:
    """
    A class of data for a sales person
    """

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return bool(self.total_sales() >= quota)

    def compare_to(self, other):
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())
