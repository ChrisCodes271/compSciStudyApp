from tkinter import *
import auxFunctions
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Variables tracked by the entire application.
question_tally = 0
correct_answer_tally = 0

# Root window setup
root = customtkinter.CTk()
root.geometry(f"{800}x{800}") 
root.title("Roadmap.sh Study Utility")
icon = PhotoImage(file='logo.png')
root.iconphoto(TRUE, icon) # Icon support on Windows (Currently does nothing on Mac (Unix based OS's))

# Frame app runs inside. Variable is used frequently throughout.  
frame = customtkinter.CTkFrame(master=root) 
frame.pack(pady=20, padx=40, fill="both", expand=True) 

textbox = customtkinter.CTkTextbox(frame)
textbox.grid(row=0, column=0)
textbox.insert("0.0", "You have gotten " + str(correct_answer_tally) + " questions right, out of " + str(question_tally) + " total questions!")
text = textbox.get("0.0", "end")
textbox.configure(state="disabled")
textbox.pack()

# Menu bar 
menu_bar = Menu(frame, background='purple', foreground='black', activebackground='black', activeforeground='purple')

# Settings for "File" tab of the Menu bar. 
file = Menu(menu_bar,tearoff=0)
file.add_command(label="New Test Bank", command=auxFunctions.create_test_bank)
file.add_command(label="Delete Test Bank", command=auxFunctions.delete_test_bank)
menu_bar.add_cascade(label="Database",menu=file)

# Settings for "Edit" tab of the Menu bar
edit = Menu(menu_bar, tearoff=0)
edit.add_command(label="New Flash Card",command=auxFunctions.new_flashcard)
edit.add_command(label="Delete Flash Card",command=auxFunctions.delete_flashcard)
menu_bar.add_cascade(label="Edit",menu=edit)

# Generate quiz button in frame. Pass frame as anon to auxfunctions to generateS data. 
quiz_button = customtkinter.CTkButton(master=frame, text="New Quiz", command=lambda: auxFunctions.new_question(frame))
quiz_button.pack()

root.config(menu=menu_bar)
root.mainloop()
