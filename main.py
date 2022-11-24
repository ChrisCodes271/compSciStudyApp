from tkinter import *
import buttons

window = Tk()
window.geometry("800x800")
window.title("Roadmap.sh FlashCards (CompSci)")
icon = PhotoImage(file='logo.png')
window.iconphoto(TRUE, icon)

# Section of buttons. Referenced functions can be found in buttons module.
buttons.add_test_bank_button(window)
buttons.delete_test_bank_button(window)
buttons.add_flashcard_button(window)
buttons.delete_flashcard_button(window)
buttons.new_question_button(window)

window.mainloop()
