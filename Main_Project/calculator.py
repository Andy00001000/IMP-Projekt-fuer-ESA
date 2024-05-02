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


    Tmax_label = ctk.CTkLabel(calcapp, text="Tmax:")
    Tmax_label.grid(row=0, column=0)
    Tmax_entry = ctk.CTkEntry(calcapp)
    Tmax_entry.grid(row=0, column=1)

    dt_label = ctk.CTkLabel(calcapp, text="dt:")
    dt_label.grid(row=1, column=0)
    dt_entry = ctk.CTkEntry(calcapp)
    dt_entry.grid(row=1, column=1)

    v0_label = ctk.CTkLabel(calcapp, text="v0:")
    v0_label.grid(row=2, column=0)
    v0_entry = ctk.CTkEntry(calcapp)
    v0_entry.grid(row=2, column=1)

    rho_label = ctk.CTkLabel(calcapp, text="rho:")
    rho_label.grid(row=3, column=0)
    rho_entry = ctk.CTkEntry(calcapp)
    rho_entry.grid(row=3, column=1)

    A_label = ctk.CTkLabel(calcapp, text="A:")
    A_label.grid(row=4, column=0)
    A_entry = ctk.CTkEntry(calcapp)
    A_entry.grid(row=4, column=1)

    cw_label = ctk.CTkLabel(calcapp, text="cw:")
    cw_label.grid(row=5, column=0)
    cw_entry = ctk.CTkEntry(calcapp)
    cw_entry.grid(row=5, column=1)

    m_label = ctk.CTkLabel(calcapp, text="m:")
    m_label.grid(row=6, column=0)
    m_entry = ctk.CTkEntry(calcapp)
    m_entry.grid(row=6, column=1)

    g_label = ctk.CTkLabel(calcapp, text="g:")
    g_label.grid(row=7, column=0)
    g_entry = ctk.CTkEntry(calcapp)
    g_entry.grid(row=7, column=1)





    button = ctk.CTkButton(calcapp, text="Home", command=button_callback)
    calcbutton = ctk.CTkButton(calcapp, tetx="Calculate", command=calculate_button)



    calculate_button.pack(padx=20, pady=20)
    button.pack(padx=20, pady=20, side="bottom")

    calcapp.mainloop()



