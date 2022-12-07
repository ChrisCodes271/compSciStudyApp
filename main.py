from tkinter import *
import auxFunctions
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk() # Initialize main window
root.geometry(f"{800}x{800}") # Set size to 800 x 800
root.title("Roadmap.sh Study Utility") # App title
icon = PhotoImage(file='logo.png') # Set icon variable
root.iconphoto(TRUE, icon) # Icon support on Windows (Currently does nothing on Mac (Unix based OS's))

frame = customtkinter.CTkFrame(master=root) # Generate frame for future use. 
frame.pack(pady=20, padx=40, fill="both", expand=True) # Set padding from main window, and pack

# Menu bar settings. 
menu_bar = Menu(frame, background='purple', foreground='black', activebackground='black', activeforeground='purple')

# Settings for "File" tab of the menu bar. 
file = Menu(menu_bar,tearoff=0)
file.add_command(label="New Test Bank", command=auxFunctions.create_test_bank)
file.add_command(label="Delete Test Bank", command=auxFunctions.delete_test_bank)
menu_bar.add_cascade(label="Database",menu=file)

# Settings for "Edit" tab of the menu bar
edit = Menu(menu_bar, tearoff=0)
edit.add_command(label="New Flash Card",command=auxFunctions.new_flashcard)
edit.add_command(label="Delete Flash Card",command=auxFunctions.delete_flashcard)
menu_bar.add_cascade(label="Edit",menu=edit)

root.config(menu=menu_bar)
root.mainloop()
