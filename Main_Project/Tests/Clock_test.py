import tkinter as tk
import time

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Uhr")
        self.time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
        self.time_label.pack(anchor='center')
        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
