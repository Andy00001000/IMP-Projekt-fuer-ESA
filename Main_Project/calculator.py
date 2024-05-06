import time
import customtkinter as ctk
import time
import datetime
import tkinter as tk



def calculator_main():
    







    def button_callback():
        print("button clicked")
        calcapp.destroy()
        import main_ui

    def calculate_button():
        print("button clicked")
        

    calcapp = ctk.CTk()
    calcapp.geometry("400x150")

    #constants:
    



    dp_label = ctk.CTkLabel(calcapp, text="Delta Impuls:") #delta impuls
    dp_label.grid(row=0, column=0)
    dp_entry = ctk.CTkEntry(calcapp)
    dp_entry.grid(row=0, column=1)

    ve_label = ctk.CTkLabel(calcapp, text="Geschwindigkeit:") #Geschwindigkeit
    ve_label.grid(row=1, column=0)
    ve_entry = ctk.CTkEntry(calcapp)
    ve_entry.grid(row=1, column=1)

    dm_label = ctk.CTkLabel(calcapp, text="Delta Masse:") #delta masse
    dm_label.grid(row=2, column=0)
    dm_entry = ctk.CTkEntry(calcapp)
    dm_entry.grid(row=2, column=1)

    dt_label = ctk.CTkLabel(calcapp, text="Delta Zeit:") #delta zeit
    dt_label.grid(row=3, column=0)
    dt_entry = ctk.CTkEntry(calcapp)
    dt_entry.grid(row=3, column=1)

    cw_label = ctk.CTkLabel(calcapp, text="Strömungswiderstandsbeiwert:") #Strömungswiderstandsbeiwert
    cw_label.grid(row=4, column=0)
    cw_entry = ctk.CTkEntry(calcapp)
    cw_entry.grid(row=4, column=1)

    p_label = ctk.CTkLabel(calcapp, text="Luftdichte:") #Luftdichte
    p_label.grid(row=5, column=0)
    p_entry = ctk.CTkEntry(calcapp)
    p_entry.grid(row=5, column=1)

    A_label = ctk.CTkLabel(calcapp, text="Frontfläche:") #Frontfläche
    A_label.grid(row=6, column=0)
    A_entry = ctk.CTkEntry(calcapp)
    A_entry.grid(row=6, column=1)

    v_label = ctk.CTkLabel(calcapp, text="Geschwindigkeit:") #Geschwindigkeit
    v_label.grid(row=7, column=0)
    v_entry = ctk.CTkEntry(calcapp)
    v_entry.grid(row=7, column=1)

    h_label = ctk.CTkLabel(calcapp, text="Höhe:") #Höhe
    h_label.grid(row=8, column=0)
    h_entry = ctk.CTkEntry(calcapp)
    h_entry.grid(row=8, column=1)

    p0_label = ctk.CTkLabel(calcapp, text="Luftdichte:") #Luftdichte auf Meereshöhe
    p0_label.grid(row=9, column=0)
    p0_entry = ctk.CTkEntry(calcapp)
    p0_entry.grid(row=9, column=1)

    g_label = ctk.CTkLabel(calcapp, text="Erdbeschleunigung:") #Erdbeschleunigung
    g_label.grid(row=10, column=0)
    g_entry = ctk.CTkEntry(calcapp)
    g_entry.grid(row=10, column=1)

    M_label = ctk.CTkLabel(calcapp, text="Die mittlere molare Masse der Luft:") #M die mittlere molare Masse der Luft
    M_label.grid(row=11, column=0)
    M_entry = ctk.CTkEntry(calcapp)
    M_entry.grid(row=11, column=1)

    R_label = ctk.CTkLabel(calcapp, text="Die allgemeine Gaskonstante:") #die allgemeine Gaskonstante
    R_label.grid(row=12, column=0)
    R_entry = ctk.CTkEntry(calcapp)
    R_entry.grid(row=12, column=1)

    varm_label = ctk.CTkLabel(calcapp, text="Geschwindigkeit:") #Geschwindigkeit von Armstrong
    varm_label.grid(row=13, column=0)
    varm_entry = ctk.CTkEntry(calcapp)
    varm_entry.grid(row=13, column=1)

    T_label = ctk.CTkLabel(calcapp, text="Temperatur der Luft:") #Temperatur der Luft
    T_label.grid(row=14, column=0)
    T_entry = ctk.CTkEntry(calcapp)
    T_entry.grid(row=14, column=1)

    a_label = ctk.CTkLabel(calcapp, text="Beschleunigung:") #Beschleunigung
    a_label.grid(row=15, column=0)
    a_entry = ctk.CTkEntry(calcapp)
    a_entry.grid(row=15, column=1)

    s_label = ctk.CTkLabel(calcapp, text="Zurückgelegte Strecke:") #Zurückgelegte Strecke s
    s_label.grid(row=16, column=0)
    s_entry = ctk.CTkEntry(calcapp)
    s_entry.grid(row=16, column=1)

    button = ctk.CTkButton(calcapp, text="Home", command=button_callback)
    calcbutton = ctk.CTkButton(calcapp, text="Calculate", command=calculate_button)



    calcbutton.grid(row = 17, column=1)
    button.grid(row = 18, column=1)

    calcapp.mainloop()



