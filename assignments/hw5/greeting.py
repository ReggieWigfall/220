"""
Name: Reginald Wigfall
greeting.py

Problem: Write a program that displays a heart with an arrow shooting through it

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from time import sleep
from graphics import GraphWin, Text, Circle, Polygon, Line, Point


def main():
    # Draw window and text object
    win = GraphWin("Greeting", 400, 400)
    win.setBackground("pink")
    greeting = Text(Point(200, 40), "Happy Valentine's Day!")
    greeting.draw(win)
    # Draw a heart in 3 parts
    heart_left = Circle(Point(182, 175), 60)
    heart_right = Circle(Point(195, 175), 60)

    heart_left.setFill('red3')
    heart_right.setFill('red3')

    heart_left.setOutline('red3')
    heart_right.setOutline('red3')

    heart_left.draw(win)
    heart_right.draw(win)

    heart_top = Polygon(Point(173.0, 113.0), Point(211.0, 113.0), Point(190.0, 123.0))
    heart_top.setFill('pink')
    heart_top.setOutline('pink')
    heart_top.draw(win)

    heart_bottom = Polygon(Point(153.0, 227.0), Point(237.0, 217.0), Point(186.0, 288.0))
    heart_bottom.setFill('red3')
    heart_bottom.setOutline('red3')
    heart_bottom.draw(win)

    # Draw arrow
    arrow = Line(Point(5, 175), Point(60, 175))
    arrow.setOutline('red')
    arrow.setArrow("last")
    arrow.draw(win)

    # Make arrow move across screen
    for greeting in range(20):
        arrow.move(20, 0)
        sleep(.1)

    # Create exit message and wait for user input
    close_message = Text(Point(200, 380), "Click anywhere to close")
    close_message.draw(win)
    win.getMouse()


if __name__ == '__main__':
    main()
