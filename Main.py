import tkinter as tk
from Main_frame import MainFrame
from FSM_Generator_frame import FSM_Generator
from Mutants_Generator_frame import Mutants_Generator
from Mutants_Testing_frame import Mutants_Testing

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("FSM Tools")
        self.geometry("1000x500")

        self.current_frame = None
        self.frames = {}

        self.create_frames()
        self.show_frame("Main")

    def create_frames(self):
        # Create frames for different interfaces
        self.frames["Main"] = MainFrame(self)
        self.frames["FSM Generator"] = FSM_Generator(self)
        self.frames["Mutants Generator"] = Mutants_Generator(self)
        self.frames["Mutants Testing"] = Mutants_Testing(self)

    def show_frame(self, page_name):
        # Show the requested frame
        frame = self.frames[page_name]
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack(expand=True, fill="both")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
