"""
Name: Reginald Wigfall
bumper.py

Problem: Write a program that creates two circles that move and collide

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
import math
from random import randint
from time import sleep
from graphics import GraphWin, Circle, Point, color_rgb


def get_random(move_amount):
    return randint(min(-move_amount, move_amount), max(-move_amount, move_amount))


def did_collide(ball, ball2):
    center1 = ball.getCenter()
    center2 = ball2.getCenter()
    radius1 = ball.getRadius()
    radius2 = ball2.getRadius()
    return bool(math.sqrt((center1.getX() - center2.getX()) ** 2 +
                          (center1.getY() - center2.getY()) ** 2) <= radius1 + radius2)


def hit_vertical(ball, win):
    center = ball.getCenter()
    radius = ball.getRadius()
    height = win.getHeight()
    width = win.getWidth()
    if (center.getY()) >= height or (center.getY()) <= 0.0:
        return True
    return bool((center.getX() + radius) >= width or (center.getX() - radius) <= 0)


def hit_horizontal(ball, win):
    center = ball.getCenter()
    radius = ball.getRadius()
    width = win.getWidth()
    height = win.getHeight()
    if (center.getX()) >= width or (center.getX()) <= 0:
        return True
    return bool((center.getY() + radius) >= height or (center.getY() - radius) <= 0.0)


def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def main():
    # Draw window and circles
    win = GraphWin("Bumper", 400, 400)
    ball1 = Circle(Point(100, 200), 25)
    ball1.setFill(color_rgb(*get_random_color()))

    ball2 = Circle(Point(200, 200), 25)
    ball2.setFill(color_rgb(*get_random_color()))

    ball1.draw(win)
    ball2.draw(win)

    ball1_dx = get_random(5)
    ball1_dy = get_random(5)
    ball2_dx = get_random(5)
    ball2_dy = get_random(5)
# Run indefinite loop to make the balls move
    while True:
        # Determines how fast the loop runs
        sleep(.01)

        ball1.move(ball1_dx, ball1_dy)
        ball2.move(ball2_dx, ball2_dy)
# Make balls move in opposite directions if they collide or hit a wall
        if did_collide(ball1, ball2):
            ball1_dx = -ball1_dx
            ball1_dy = -ball2_dy
            ball2_dx = -ball2_dx
            ball2_dy = -ball2_dy

        if hit_horizontal(ball1, win):
            ball1_dx = -ball1_dx
        if hit_vertical(ball1, win):
            ball1_dy = -ball1_dy

        if hit_horizontal(ball2, win):
            ball2_dx = -ball2_dx
        if hit_vertical(ball2, win):
            ball2_dy = -ball2_dy


if __name__ == '__main__':
    main()
