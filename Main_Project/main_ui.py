import time
import customtkinter as ctk
import time
import datetime
import tkinter as tk
from playsound import playsound


def button_callback():
    playsound('C:/Users/andi.schmidt/Documents/Schule/IMP/Projekt/Main_Project/bark.wav')
    import calculator2
    root.destroy()
    calculator2.calculator_main()

root = ctk.CTk()
root.geometry("400x150")
root.title("Launcher")



clock = ctk.CTkLabel(root, text="")
button = ctk.CTkButton(root, text="Open Calculator", command=button_callback)

#test

#testtest

class ClockLabel(ctk.CTkLabel):
    def __init__(self, master=None, **kwargs):
        ctk.CTkLabel.__init__(self, master, **kwargs)
        self.update_time()
        playsound('C:/Users/andi.schmidt/Documents/Schule/IMP/Projekt/Main_Project/bark.wav')

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.configure(text=current_time)
        self.after(1000, self.update_time)
        

#test



#root.clock_label = ClockLabel(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
root.clock_label = ClockLabel(root)

#Packer, der alle Elemente tatsächlich einbaut
button.pack(padx=20, pady=20)
root.clock_label.pack(anchor='center', pady=20)
root.mainloop()