import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label = tk.Label(self, text="Choose one of the options:", font=("Helvetica", 18))
        label.pack(pady=20)

        options = ["FSM Generator", "Mutants Generator", "Mutants Testing"]
        for option in options:
            button = tk.Button(self, text=option, command=lambda opt=option: self.master.show_frame(opt))
            button.pack(pady=10)
