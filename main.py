# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from typing import Optional


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = tk.Tk()
    greeting = label = tk.Label(
        text="Did you really think, i can do anything, Koblížku?",
        foreground="white",  # Set the text color to white
        background="black", # Set the background color to black
        width=100,
        height=10
    )
    greeting.pack()
    window.mainloop()
    print_hi('PyCharm')


def openExcel(path):
    print(f'{path}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
