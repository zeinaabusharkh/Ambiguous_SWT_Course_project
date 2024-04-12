import tkinter as tk
from tkinter import filedialog

class Mutants_Generator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Heading
        heading_label = tk.Label(self, text="Mutant's Generator", font=("Helvetica", 24))
        heading_label.pack(pady=20)

        # upload entry
        upload_frame = tk.Frame(self)
        upload_frame.pack()

        tk.Label(upload_frame, text="Choose FSM file:").pack(side='left', padx=7)
        self.upload_entry = tk.Entry(upload_frame)
        self.upload_entry.pack(side='left')
        upload_button = tk.Button(upload_frame, text="Upload", command=self.upload_fsm)
        upload_button.pack(side='right')


        # Number of Mutants

        mutants_frame = tk.Frame(self)
        mutants_frame.pack()
        tk.Label(mutants_frame, text="Number of Mutants:").pack(side='left', padx=7)
        self.mutants_entry = tk.Entry(mutants_frame)
        self.mutants_entry.pack(side='right')

        # Fault Types
        fault_types_frame = tk.Frame(self)
        fault_types_frame.pack(pady=10)

        fault_types_label = tk.Label(fault_types_frame, text="Fault Types:")
        fault_types_label.pack()

        self.fault_types = ["Output", "TT", "TTT of Output"]
        self.fault_vars = {}
        for fault in self.fault_types:
            var = tk.BooleanVar()
            var.set(False)
            self.fault_vars[fault] = var
            checkbox = tk.Checkbutton(fault_types_frame, text=fault, variable=var)
            checkbox.pack(anchor=tk.W)

        # Number of Faults per Mutant
        faults_per_mutant_label = tk.Label(self, text="Number of Faults per Mutant:")
        faults_per_mutant_label.pack()
        self.faults_per_mutant_entry = tk.Entry(self)
        self.faults_per_mutant_entry.pack()

        # Generate Button
        generate_button = tk.Button(self, text="Generate Mutants", command=self.generate_mutants)
        generate_button.pack(pady=20)

        back_button = tk.Button(self, text="Back", command=lambda: (self.clear_inputs(), self.master.show_frame("Main")))
        back_button.pack(pady=10)

    def upload_fsm(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select FSM file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            self.upload_entry.delete(0, tk.END)
            self.upload_entry.insert(0, filename)
            
    def clear_inputs(self):
        # Clear FSM entry
        self.upload_entry.delete(0, tk.END)
        # Clear Mutants entry
        self.mutants_entry.delete(0, tk.END)
        # Reset fault checkboxes
        for var in self.fault_vars.values():
            var.set(False)
        # Clear faults per mutant entry
        self.faults_per_mutant_entry.delete(0, tk.END)
        
    def generate_mutants(self):
        try : 
            fsm_file = self.upload_entry.get()
            num_mutants = int(self.mutants_entry.get())
            selected_faults = [fault for fault, var in self.fault_vars.items() if var.get()]
            num_faults_per_mutant = int(self.faults_per_mutant_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid integer values for number of mutants and number of faults per mutants.")
            return
        
        # testings
        
        print("FSM file:", fsm_file)
        print("Number of Mutants:", num_mutants)
        print("Selected Faults:", selected_faults)
        print("Number of Faults per Mutant:", num_faults_per_mutant)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frames = {}
        for F in (Mutants_Generator,):
            frame = F(self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Mutants_Generator")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

