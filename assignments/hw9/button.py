"""
Name: Reginald Wigfall

button.py

Problem: Create a button class to use in the GUI of the three button game

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""
from graphics import Text


class Button:
    """
    A class to create a button
    """
    def __init__(self, shape, label):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        point_x = point.getX()
        point_y = point.getY()
        button_p1 = self.shape.getP1()
        button_p2 = self.shape.getP2()
        button_x1 = button_p1.getX()
        button_y1 = button_p1.getY()
        button_x2 = button_p2.getX()
        button_y2 = button_p2.getY()
        return bool(button_x1 <= point_x <= button_x2 and button_y1 <= point_y <= button_y2)

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
