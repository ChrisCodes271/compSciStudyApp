import auxFunctions
from tkinter import *


def add_test_bank_button(window):
    button = Button(window,
                    text='Create new test bank.',
                    command=auxFunctions.create_test_bank(),
                    font=('Arial', 25),
                    )
    button.pack()


def delete_test_bank_button(window):
    button = Button(window,
                    text='Delete existing test bank.',
                    command=auxFunctions.delete_test_bank,
                    font=('Arial', 25),
                    )
    button.pack()


def add_flashcard_button(window):
    button = Button(window,
                    text='New Flashcard',
                    command=auxFunctions.new_flashcard,
                    font=('Arial', 25))
    button.pack()


def delete_flashcard_button(window):
    button = Button(window,
                    text='Delete Flashcard',
                    command=auxFunctions.delete_flashcard,
                    font=('Arial', 25))
    button.pack()


def new_quiz_button(window):
    button = Button(window,
                    text='New Quiz',
                    command=auxFunctions.new_quiz,
                    font=('Arial', 25))
    button.pack()
