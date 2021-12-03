"""
Name: Reginald Wigfall
sales_force.py

Problem: Write a class of data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from sales_person import SalesPerson


class SalesForce:
    """
    A class of data for a sales person
    """

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name) as in_file:
            file = in_file.readlines()
        for line in file:
            employee_id, name, sale_amount = line.split(",")
            sales_person = SalesPerson(employee_id, name)
            for sale in sale_amount.split():
                sales_person.enter_sale(float(sale))
            self.sales_people.append(sales_person)

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            seller = [person.employee_id, person.name,
                      person.total_sales(), person.met_quota(quota)]
            report.append(seller)
        return report

    def top_seller(self):
        highest_seller = dict()
        for person in self.sales_people:
            if person.total_sales() in highest_seller:
                highest_seller[person.total_sales()].append(person)
            else:
                highest_seller[person.total_sales()] = [person]
        sorted_highest = sorted(highest_seller, reverse=True)
        return highest_seller[sorted_highest[0]]

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if str(employee_id) == str(person.employee_id):
                return person
        return None
