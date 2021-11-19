"""
Name: Reginald Wigfall

threeDoorGame.py

Problem: Create a three door game where user has to guess a random door

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

from graphics import GraphWin, Text, Rectangle, Point
from button import Button
from random import randint


def main():
    win = GraphWin("Three Button Game", 400, 350)

    # Create initial text for game
    text1 = Text(Point(200, 20), "I have a secret door")
    text1.draw(win)
    text2 = Text(Point(200, 300), "Click to guess my door")
    text2.draw(win)

    # Create and label doors for user to click on

    shape1 = Rectangle(Point(20, 70), Point(100, 250))
    door1 = Button(shape1, "Door1")
    door1.draw(win)
    shape2 = Rectangle(Point(120, 70), Point(200, 250))
    door2 = Button(shape2, "Door2")
    door2.draw(win)
    shape3 = Rectangle(Point(220, 70), Point(300, 250))
    door3 = Button(shape3, "Door3")
    door3.draw(win)

    # Choose the secret door
    secret_door = randint(1, 3)

    # Wait for user guess the door with mouse click
    point = win.getMouse()

    # Check if user guessed correctly and notify them
    if door1.is_clicked(point) and secret_door == 1:
        door1.color_button("green")
        text1.setText("You win!")
        text2.setText("Click to close")
    elif door2.is_clicked(point) and secret_door == 2:
        door2.color_button("green")
        text1.setText("You win!")
        text2.setText("Click to close")
    elif door3.is_clicked(point) and secret_door == 3:
        door3.color_button("green")
        text1.setText("You win!")
        text2.setText("Click to close")

    # Notify user they lost and reveal correct door
    else:
        text1.setText("You Lose!")
        text2.setText("Door {0} was my secret door".format(secret_door))
        if door1.is_clicked(point):
            door1.color_button("red")
        if door2.is_clicked(point):
            door2.color_button("red")
        if door3.is_clicked(point):
            door3.color_button("red")
    win.getMouse()


if __name__ == "__main__":
    main()
