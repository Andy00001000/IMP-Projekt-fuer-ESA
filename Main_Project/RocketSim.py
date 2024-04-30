import customtkinter as ctk


def RocketSim_main():
    def button_callback():
        print("button clicked")
        app2.destroy()
        import main_ui

    app2 = ctk.CTk()
    app2.geometry("400x150")

    button = ctk.CTkButton(app2, text="Home", command=button_callback)
    button.pack(padx=20, pady=20)

    app2.mainloop()






