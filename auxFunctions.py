import databaseFunctions
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


def new_question():
    try:
        correct_card = databaseFunctions.retrieve_random_card()
        # question = correct_card[0]
        correct_answer = correct_card[1]
        other_answers = dict()
        other_answers[0] = ''
        other_answers[1] = ''
        other_answers[2] = ''
        i = 3
        j = 0
        while i > 0:
            test_value = databaseFunctions.retrieve_random_answer()
            if test_value != correct_answer:
                if test_value != other_answers[0] and test_value != other_answers[1] and test_value != other_answers[2]:
                    other_answers[j] = test_value
                    i -= 1
                    j += 1
        print(other_answers)
        print(correct_answer)

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


new_question()
