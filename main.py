import tkinter as tk
from tkinter import messagebox
import customtkinter as ct


# Create the main tkinter window
root = ct.CTk()
root.geometry("700x400")
root.title("Telemetry Data Organizer")
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

#Title Text
label = ct.CTkLabel(root, text="INFO 103 Project", font = ('Arial', 20))
label.pack(padx=20, pady=20)

# Create a frame for the button
buttonframe = ct.CTkFrame(root)
buttonframe.pack(padx=20, pady=40)


tk.mainloop()