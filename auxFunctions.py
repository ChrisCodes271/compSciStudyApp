import databaseFunctions
import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import random


def create_test_bank():  # Function to generate new test bank. Called in the add test bank button.
    try:
        databaseFunctions.create_table()

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def delete_test_bank():  # Function to delete existing test bank. Called in the delete test bank button.
    try:
        databaseFunctions.delete_table()

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def new_flashcard():  # New flashcard function used in the add flash card button.
    # Then pass to database function.  Request user input for card front and card back.
    try:
        card_front = simpledialog.askstring(title='Card Front',
                                            prompt='Whats on the front of your flashcard?', )
        card_back = simpledialog.askstring(title='Card Back',
                                           prompt='Whats on the back?')
        databaseFunctions.new_entry(card_front, card_back)

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def delete_flashcard():  # Request what card to erase. Currently, requires SQL Entry ID.
    try:
        card_id = simpledialog.askstring(title='Card Number',
                                         prompt='What card number would you like to erase?')
        databaseFunctions.delete_entry(card_id)

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def gen_question_data():
    card_data = databaseFunctions.retrieve_card_data()
    question = card_data[0]  # Retrieve question from correct card.
    correct_answer = card_data[1]
    answer_bank = [card_data[1], card_data[2], card_data[3], card_data[4]]
    random.shuffle(answer_bank)
    return question, correct_answer, answer_bank


def new_question(frame):
    for widgets in frame():
        widgets.destroy()
    question_data = gen_question_data()
    question = question_data[0]
    correct_answer = question_data[1]
    answer_bank = question_data[2]
    messagebox.showinfo(title="Question!", message=question)
    button1 = Button(frame,
                     text=answer_bank[0],
                     command=lambda : submit(answer_bank[0], correct_answer))
    button2 = Button(frame,
                     text=answer_bank[1],
                     command=lambda: submit(answer_bank[1], correct_answer))
    button3 = Button(frame,
                     text=answer_bank[2],
                     command=lambda: submit(answer_bank[2], correct_answer))
    button4 = Button(frame,
                     text=answer_bank[3],
                     command=lambda: submit(answer_bank[3], correct_answer))
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    


def submit(chosen_answer, correct_answer):
    print(chosen_answer)
    print(correct_answer)
    if chosen_answer == correct_answer:
        messagebox.showinfo("CORRECT")
    else:
        messagebox.showinfo("WRONG")
