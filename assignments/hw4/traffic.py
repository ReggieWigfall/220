"""
Name: Reginald Wigfall
traffic.py
Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    total_cars = 0
    cars = 0

    # Ask user for number of roads surveyed
    num_roads = eval(input("How many roads were surveyed? "))

    # Run for loop for each road surveyed
    for i in range(num_roads):
        days = eval(input("How many days was road {} surveyed? " .format(i + 1)))
        # Run nested loop that asks how many cars traveled on each day
        for j in range(days):
            cars = cars + (eval(input("How many cars traveled on day {}? " .format(j + 1))))
        # Print average number of vehicles per day
        average_cars = cars / days
        print("Road", i + 1, "average vehicles per day: ",  round(average_cars, 2))
        # Store total number of cars traveled
        total_cars = total_cars + cars
        # Reset number of cars traveled for the next day
        cars = 0
        # Output total number of cars traveled and average number of cars per road
    print("Total number of vehicles traveled on all roads: ", total_cars)
    print("Average number of vehicles per road: ", round(total_cars / num_roads, 2))


if __name__ == '__main__':
    main()
