import databaseFunctions
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def create_test_bank():
    try:
        databaseFunctions.create_table()

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def delete_test_bank():
    try:
        databaseFunctions.delete_table()

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def new_flashcard():
    try:
        card_front = simpledialog.askstring(title='Card Front',
                                            prompt='Whats on the front of your flashcard?', )
        card_back = simpledialog.askstring(title='Card Back',
                                           prompt='Whats on the back?')
        databaseFunctions.new_entry(card_front, card_back)

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def delete_flashcard():
    try:
        card_id = simpledialog.askstring(title='Card Number',
                                         prompt='What card number would you like to erase?')
        databaseFunctions.delete_entry(card_id)

    except Exception as e:
        messagebox.showerror(title="An Error Occured", message=str(e))


def add_test_bank_button(window):
    button = Button(window,
                    text='Create new test bank.',
                    command=create_test_bank,
                    font=('Arial', 25),
                    )
    button.pack()


def delete_test_bank_button(window):
    button = Button(window,
                    text='Delete existing test bank.',
                    command=delete_test_bank,
                    font=('Arial', 25),
                    )
    button.pack()


def add_flashcard_button(window):
    button = Button(window,
                    text='New Flashcard',
                    command=new_flashcard,
                    font=('Arial', 25))
    button.pack()


def delete_flashcard_button(window):
    button = Button(window,
                    text='Delete Flashcard',
                    command=delete_flashcard,
                    font=('Arial', 25))
    button.pack()
