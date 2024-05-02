import time
import customtkinter as ctk
import time
import datetime
import tkinter as tk



def calculator_main():
    


    def button_callback():
        print("button clicked")
        calcapp.destroy()
        import Main_Project.Tests.main_ui_old as main_ui_old

    def calculate_button():
        print("button clicked")
        

    calcapp = ctk.CTk()
    calcapp.geometry("400x150")

    button = ctk.CTkButton(calcapp, text="Home", command=button_callback)
    calcbutton = ctk.CTkButton(calcapp, tetx="Calculate", command=calculate_button)



    calculate_button.pack(padx=20, pady=20)
    button.pack(padx=20, pady=20, side="bottom")

    calcapp.mainloop()



