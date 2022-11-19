from tkinter import *
import buttons

window = Tk()
window.geometry("800x800")
window.title("Roadmap.sh FlashCards (CompSci)")
icon = PhotoImage(file='logo.png')
window.iconphoto(TRUE, icon)

buttons.add_test_bank_button(window)
buttons.delete_test_bank_button(window)
buttons.add_flashcard_button(window)
buttons.delete_flashcard_button(window)

window.mainloop()
