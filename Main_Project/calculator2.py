import numpy as np
import matplotlib.pyplot as plt
import customtkinter as ctk
import ctypes
from tkinter import *
from tkinter import messagebox
from playsound import playsound

def calculator_main():

    def error_win(error_titel, eror_message):
        for bark in range(1, 4):
            playsound('C:/Users/andi.schmidt/Documents/Schule/IMP/Projekt/Main_Project/bark.wav')
        messagebox.showerror(error_titel, eror_message)
        




    def calculate_and_plot():
        

        
            try:
                
                
                # Holen der eingegebenen Werte aus den Eingabefeldern
                Tmax = float(Tmax_entry.get().replace(",", "."))
                #dt = float(dt_entry.get().replace(",", "."))
                v0 = float(v0_entry.get().replace(",", "."))
                #rho = float(rho_entry.get().replace(",", "."))
                A = float(A_entry.get().replace(",", "."))
                cw = float(cw_entry.get().replace(",", "."))
                m = float(m_entry.get().replace(",", "."))
                #g = float(g_entry.get().replace(",", "."))
                
    

                #drinnen für Debugging
                
                #Tmax = 5
                dt = 1
                #v0 = 2
                rho = 1.29
                #A = 0.00126
                #cw = 0.45
                #m = 0.0027
                g = 9.81
                
            
            
                time = np.zeros(int(Tmax/dt))
                velocity = np.zeros(int(Tmax/dt))
                acc = np.zeros(int(Tmax/dt))
                dist = np.zeros(int(Tmax/dt))

                velocity[0] = v0
                dist[0] = 0

                for x in range(time.size-1):
                    time[x+1] = time[x] + dt
                    acc[x] = g - (1/2 * ((cw * rho * A)/m) * pow(velocity[x], 2))
                    incV = acc[x] * dt
                    velocity[x+1] = velocity[x] + incV
                    dist[x+1] = dist[x] + velocity[x] * dt

                # Erstellen des Plots
                plt.figure(figsize=(10, 6))

                plt.subplot(3, 1, 1)
                plt.plot(dist)
                plt.xlabel('Zeit in Sekunden')
                plt.ylabel('Höhe in Meter')
                plt.title('Höhe-Zeit-Diagramm')
                plt.tight_layout()
                plt.show()
                #print("Done")
                playsound('C:/Users/andi.schmidt/Documents/Schule/IMP/Projekt/Main_Project/bark.wav')

                

            except:
                for bark in range(1, 4):
                    playsound('C:/Users/andi.schmidt/Documents/Schule/IMP/Projekt/Main_Project/bark.wav')
                error_win("Value Error","Error calculating Value, likely due to invalid input")







    # Erstellen des Hauptfensters
    root = ctk.CTk()
    root.title('Physiksimulator')



    #Checkboxen für welche Graphen gezeigt werden
    """
    def checkbox1_event():
        print("checkbox toggled, current value:", check1_var.get())

    def checkbox2_event():
        print("checkbox toggled, current value:", check2_var.get())

    def checkbox3_event():
        print("checkbox toggled, current value:", check1_var.get())
    """




    # Erstellen der Eingabefelder für die Werte
    Tmax_label = ctk.CTkLabel(root, text="Geben sie den Berechnungszeitraum Tmax in Sekunden:")
    Tmax_label.grid(row=0, column=0)
    Tmax_entry = ctk.CTkEntry(root)
    Tmax_entry.grid(row=0, column=1)

    """
    dt_label = ctk.CTkLabel(root, text="Geben sie die größe der Zeitschritte dt in:")
    dt_label.grid(row=1, column=0)
    dt_entry = ctk.CTkEntry(root)
    dt_entry.grid(row=1, column=1)
    """

    v0_label = ctk.CTkLabel(root, text="Geben sie die Startgeschwindigkeit v0 in m/s:")
    v0_label.grid(row=2, column=0)
    v0_entry = ctk.CTkEntry(root)
    v0_entry.grid(row=2, column=1)

    """
    rho_label = ctk.CTkLabel(root, text="rho:")
    rho_label.grid(row=3, column=0)
    rho_entry = ctk.CTkEntry(root)
    rho_entry.grid(row=3, column=1)
    """

    A_label = ctk.CTkLabel(root, text="Geben sie die Fläche A der Rakete in m^2:")
    A_label.grid(row=4, column=0)
    A_entry = ctk.CTkEntry(root)
    A_entry.grid(row=4, column=1)

    cw_label = ctk.CTkLabel(root, text="Geben sie den Strömungswiederstandswert cw:")
    cw_label.grid(row=5, column=0)
    cw_entry = ctk.CTkEntry(root)
    cw_entry.grid(row=5, column=1)

    m_label = ctk.CTkLabel(root, text="Geben die die Masse m der Rakete in kg:")
    m_label.grid(row=6, column=0)
    m_entry = ctk.CTkEntry(root)
    m_entry.grid(row=6, column=1)

    """
    g_label = ctk.CTkLabel(root, text="g:")
    g_label.grid(row=7, column=0)
    g_entry = ctk.CTkEntry(root)
    g_entry.grid(row=7, column=1)
    """


    # Schaltfläche zum Berechnen und Anzeigen des Diagramms
    calculate_button = ctk.CTkButton(root, text="Berechnen und Diagramm anzeigen", command=calculate_and_plot)
    calculate_button.grid(row=9, column=0, columnspan=2)

    root.minsize(500, 300)
    root.maxsize(500, 300)


    #print(root._current_width)
    #print(root._current_height)


    root.mainloop()
