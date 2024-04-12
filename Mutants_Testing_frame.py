import tkinter as tk
from tkinter import filedialog

class Mutants_Testing(tk.Frame):
    def __init__(self, master):
            super().__init__(master)
            self.master = master

            # Heading
            heading_label = tk.Label(self, text="Mutant's Testing", font=("Helvetica", 24))
            heading_label.pack(pady=20)

            # upload FSM
            upload_frame = tk.Frame(self)
            upload_frame.pack()

            tk.Label(upload_frame, text="Choose FSM file:").pack(side='left', padx=7)
            self.upload_entry = tk.Entry(upload_frame)
            self.upload_entry.pack(side='left')
            upload_button = tk.Button(upload_frame, text="Upload", command=self.upload_fsm)
            upload_button.pack(side='right')

            # upload Mutants
            upload_m_frame = tk.Frame(self)
            upload_m_frame.pack()

            tk.Label(upload_m_frame, text="Choose Mutant's file:").pack(side='left', padx=7)
            self.upload_m_entry = tk.Entry(upload_m_frame)
            self.upload_m_entry.pack(side='left')
            upload_m_button = tk.Button(upload_m_frame, text="Upload", command=self.upload_mutants)
            upload_m_button.pack(side='right')
            
            # Testing Button
            testing_Button = tk.Button(self, text="Perform Testing", command=self.perform_testing)
            testing_Button.pack(pady=20)

            # Save Test Cases Button
            save_test_cases_button = tk.Button(self, text="Save Test Cases", command=self.save_test_cases)
            save_test_cases_button.pack(pady=20)

            back_button = tk.Button(self, text="Back", command=lambda: (self.clear_inputs(), self.master.show_frame("Main")))
            back_button.pack(pady=10)

    def upload_fsm(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select FSM file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if filename:
                self.upload_entry.delete(0, tk.END)
                self.upload_entry.insert(0, filename)

    def upload_mutants(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select Mutants file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if filename:
                self.upload_m_entry.delete(0, tk.END)
                self.upload_m_entry.insert(0, filename)

    def clear_inputs(self):
            # Clear FSM entry
            self.upload_entry.delete(0, tk.END)
            # Clear Mutants entry
            self.upload_m_entry.delete(0, tk.END)

    def save_test_cases():
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save Test Cases", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            print("Test cases saved as:", filename)

            
    def perform_testing(self):
        try : 
            fsm_file = self.upload_entry.get()
            mutant_file = self.upload_m_entry.get()
        except ValueError:  
                tk.messagebox.showerror("Error", "Please upload the FSM File and the Mutant's File.")
                return 
            # testings
        print("FSM file:", fsm_file)
        print("Mutant file:", mutant_file)



class MainApplication(tk.Tk):
        def __init__(self):
            super().__init__()

            self.frames = {}
            for F in (Mutants_Testing,):
                frame = F(self)
                self.frames[F.__name__] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("Mutants_Testing")

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

if __name__ == "__main__":
        app = MainApplication()
        app.mainloop()


