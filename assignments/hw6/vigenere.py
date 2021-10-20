"""
Name: Reginald Wigfall
vigenere.py

Problem: Write a program to implement a vigenere cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *


def code(message, keyword):
    acc = ""
    m = message
    k = keyword
    m = m.upper()
    k = k.upper()
    m = m.replace(" ", "")
    k = k.replace(" ", "")
    for i in range(len(m)):
        m_len = m[i]
        key = k[i % len(k)]
        print(key)
        ord_m = ord(m_len) - 65
        ord_key = ord(key) - 65
        ord_encode = ((ord_key + ord_m) % 26) + 65
        chr_encode = chr(ord_encode)
        acc = acc + chr_encode
    return acc


def main():
    win = GraphWin("Vigenere", 600, 400)

    # message input text and box
    message_input_text = Text(Point(100, 60), "Message to code")
    message_input_text.draw(win)
    message_input_box = Entry(Point(310, 60), 30)
    message_input_box.draw(win)

    # keyword input text and box
    keyword_input_text = Text(Point(93, 120), "Enter Keyword")
    keyword_input_text.draw(win)
    keyword_input_box = Entry(Point(308, 120), 30)
    keyword_input_box.draw(win)

    # Encode button and text
    encode_button = Rectangle(Point(238, 150), Point(338, 220))
    encode_button.draw(win)
    encode_button_text = Text(Point(290, 185), "Encode")
    encode_button_text.draw(win)

    # Display encoded message and instruction to stop program
    win.getMouse()
    msg = message_input_box.getText()
    key = keyword_input_box.getText()
    encode_button.undraw()
    encode_button_text.setText("Resulting Message")
    encoded_message = Text(Point(290, 220), code(msg, key))
    encoded_message.draw(win)
    close_text = Text(Point(290, 380), "Click anywhere to close window")
    close_text.draw(win)
    win.getMouse()


if __name__ == '__main__':
    main()
