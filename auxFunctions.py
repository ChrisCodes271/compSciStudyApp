import databaseFunctions
import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


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


def submit(chosen_answer, correct_answer, frame):
    if chosen_answer == correct_answer:
        messagebox.showinfo("CORRECT")
    else:
        messagebox.showinfo("WRONG")
    # Destroy currently created radiobuttons in frame. 
    for widget in frame.winfo_children():
        widget_type = str(type(widget))
        if widget_type == "<class 'customtkinter.windows.widgets.ctk_radiobutton.CTkRadioButton'>":
            widget.destroy()


def new_question(frame):
    question_data = databaseFunctions.retrieve_card_data()
    question = question_data[0]
    correct_answer = question_data[1]
    answer_bank = question_data[2]
    messagebox.showinfo(title="Question!", message=question)
    choice_1 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[0], command=lambda: submit(answer_bank[0], correct_answer, frame))
    choice_2 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[1], command=lambda: submit(answer_bank[1], correct_answer, frame))
    choice_3 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[2], command=lambda: submit(answer_bank[2], correct_answer, frame))
    choice_4 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[3], command=lambda: submit(answer_bank[3], correct_answer, frame))
    choice_1.pack()
    choice_2.pack()
    choice_3.pack()
    choice_4.pack()
    
    


