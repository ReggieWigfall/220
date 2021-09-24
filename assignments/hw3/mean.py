"""
Name: Reginald Wigfall
mean.py

1) Problem: Output RMS Average, Harmonic Mean, and Geometric Mean
2) Inputs: The number of values, The values
   Outputs: RMS Average, Harmonic Mean, and Geometric mean for values entered
3) Steps:
   1. Ask user for the number of values they will enter
   2. Ask user to input a value for the number of times they entered
   3. Calculate RMS, Harmonic Mean, and Geometric Mean for the set of values
   4. Output the mean values to the user


Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
import math


def main():
    value_list = []
    rms_average = 0
    harmonic_mean = 0
    geometric_mean = 1
    # Ask user how many values they will enter
    values = eval(input("enter the number of values to be entered: "))
    # Run for loop that asks user for a value
    for i in range(values):
        value = eval(input("enter value: "))
        value_list.append(value)

    # Calculate RMS Average
    for i in range(values):
        rms_average = rms_average + (value_list[i] ** 2)

    rms_average = round(math.sqrt(rms_average / values), 3)

    # Calculate Harmonic Mean
    for i in range(values):
        harmonic_mean = harmonic_mean + (1 / value_list[i])

    harmonic_mean = round(values / harmonic_mean, 3)

    # Calculate Geometric Mean
    for i in range(values):
        geometric_mean = (geometric_mean * value_list[i])

    geometric_mean = round(geometric_mean ** (1/values), 3)

    print(rms_average)
    print(harmonic_mean)
    print(geometric_mean)


if __name__ == '__main__':
    main()
