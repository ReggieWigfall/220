"""
Name: Reginald Wigfall
weighted_average.py

Problem: Write a program that calculates the weighted average for students

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def weighted_average(in_file_name, out_file_name):
    # Open the files and initialize accumulators
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    class_average = 0
    number_of_averages = 0
    # Split names and grades
    for line in in_file:
        name, grade = line.split(":")
        grade_list = grade.split(" ")
        # Remove empty list item before continuing
        grade_list.pop(0)
        weight_acc = 0
        average_acc = 0
        for i in range(len(grade_list)):
            # Find weight in list (every 2nd value) and update its total sum
            if i % 2 == 0:
                weight_acc = weight_acc + int(grade_list[i])
            # Multiply each grade and its corresponding weight, then update the sum
            else:
                average_acc = average_acc + int(grade_list[i]) * int(grade_list[i - 1])
            # Write an error for student's average if weight doesn't total 100
        if weight_acc < 100:
            out_file.write(f"{name}'s average: Error: The weights are less than 100. \n")
        elif weight_acc > 100:
            out_file.write(f"{name}'s average: Error: The weights are more than 100. \n")
            # If weight totals 100, calculate the student's average
        else:
            number_of_averages = number_of_averages + 1
            student_average = round(average_acc / 100, 1)
            out_file.write(f"{name}'s average: {student_average} \n")
            class_average = class_average + average_acc / 100

    out_file.write(f"Class average: {round(class_average / number_of_averages, 1)}")
    # Close the files
    in_file.close()
    out_file.close()


def main():
    in_file_name = "grades.txt"
    out_file_name = "avg.txt"
    weighted_average(in_file_name, out_file_name)


if __name__ == '__main__':
    main()
