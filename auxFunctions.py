import databaseFunctions
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


def generate_question_data():  # This function will generate a question, correct answer, and 3 other answers.
                               # all answers will be stored in the answer_bank dictionary
                               # the question, correct answer, and answer_bank will be returned.
    try:
        correct_card = databaseFunctions.retrieve_random_card()
        question = correct_card[0]
        correct_answer = correct_card[1]
        answer_bank = dict()
        answer_bank[3] = correct_answer
        answer_bank[0] = ''
        answer_bank[1] = ''
        answer_bank[2] = ''
        i = 3
        j = 0
        while i > 0:
            test_value = databaseFunctions.retrieve_random_answer()
            if test_value != correct_answer:
                if test_value != answer_bank[0] and test_value != answer_bank[1] and test_value != answer_bank[2]:
                    answer_bank[j] = test_value
                    i -= 1
                    j += 1
        random.shuffle(x := list(answer_bank.values()))
        for el in enumerate(answer_bank.items()):
            answer_bank[el[1][0]] = x[el[0]]

        return answer_bank, correct_answer, question

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))


def new_question():
    x = generate_question_data()
    question = x[2]
    correct_answer = x[1]
    returned_answers = x[0]
    print(question)
    print(correct_answer)
    a = returned_answers[0]
    b = returned_answers[1]
    c = returned_answers[2]
    d = returned_answers[3]
    print("A: " + a)
    print("B: " + b)
    print("C: " + c)
    print("D: " + d)


new_question()
