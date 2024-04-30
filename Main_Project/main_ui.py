import time
import customtkinter as ctk
import time
import datetime
import tkinter as tk




def button_callback():
    import RocketSim
    root.destroy()
    RocketSim.RocketSim_main()

root = ctk.CTk()
root.geometry("400x150")
root.title("Main Menu")


clock = ctk.CTkLabel(root, text="")
button = ctk.CTkButton(root, text="RocketSim", command=button_callback)





class ClockLabel(ctk.CTkLabel):
    def __init__(self, master=None, **kwargs):
        ctk.CTkLabel.__init__(self, master, **kwargs)
        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.configure(text=current_time)
        self.after(1000, self.update_time)





#root.clock_label = ClockLabel(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
root.clock_label = ClockLabel(root)

#Packer, der alle Elemente tatsächlich einbaut
button.pack(padx=20, pady=20)
root.clock_label.pack(anchor='center', pady=20)
root.mainloop()

