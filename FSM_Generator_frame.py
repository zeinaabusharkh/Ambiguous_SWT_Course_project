import tkinter as tk

class FSM_Generator(tk.Frame):
    def __init__(self, master):
            super().__init__(master)
            self.master = master

            # Heading
            heading_label = tk.Label(self, text="FSM Generator", font=("Helvetica", 24))
            heading_label.pack(pady=20)


            # Number of States
            states_frame = tk.Frame(self)
            states_frame.pack()
            tk.Label(states_frame, text="Number of States:").pack(side='left', padx=7)
            self.states_entry = tk.Entry(states_frame)
            self.states_entry.pack(side='right')
            
            # Number of Transitions
            transitions_frame = tk.Frame(self)
            transitions_frame.pack()
            tk.Label(transitions_frame, text="Number of Transitions:").pack(side='left', padx=7)
            self.transitions_entry = tk.Entry(transitions_frame)
            self.transitions_entry.pack(side='right')

            # Number of Inputs
            inputs_frame = tk.Frame(self)
            inputs_frame.pack()
            tk.Label(inputs_frame, text="Number of inputs:").pack(side='left', padx=7)
            self.inputs_entry = tk.Entry(inputs_frame)
            self.inputs_entry.pack(side='right')

            # Number of Outputs
            outputs_frame = tk.Frame(self)
            outputs_frame.pack()
            tk.Label(outputs_frame, text="Number of outputs:").pack(side='left', padx=7)
            self.outputs_entry = tk.Entry(outputs_frame)
            self.outputs_entry.pack(side='right')


            # Fully Connected Checkbox
            fully_connected_frame = tk.Frame(self)
            fully_connected_frame.pack(pady=10)

            fully_connected_label = tk.Label(fully_connected_frame, text="fully Connected:")
            fully_connected_label.pack()

            self.fully_connected = ["fully Connected"]
            self.connected = {}
            for f in self.fully_connected:
                var = tk.BooleanVar()
                var.set(False)
                self.connected[f] = var
                checkbox = tk.Checkbutton(fully_connected_frame, text=f, variable=var)
                checkbox.pack(anchor=tk.W)


            # Generate Button
            generate_button = tk.Button(self, text="Generate FSM", command=self.FSM_generate)
            generate_button.pack(pady=20)

            back_button = tk.Button(self, text="Back", command=lambda: (self.clear_inputs(), self.master.show_frame("Main")))
            back_button.pack(pady=10)


    def clear_inputs(self):
            # Clear states entry
            self.states_entry.delete(0, tk.END)
            # Clear Transitions entry
            self.transitions_entry.delete(0, tk.END)
            # Clear inputs entry
            self.inputs_entry.delete(0, tk.END)
            # Clear outputs entry
            self.outputs_entry.delete(0, tk.END)
            # Reset checkboxes
            for var in self.connected.values():
                var.set(False)

            
    def FSM_generate(self):
        try:
            num_states = int(self.states_entry.get())
            num_inputs = int(self.inputs_entry.get())
            num_outputs = int(self.outputs_entry.get())
            num_transition = int(self.transitions_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid integer values for states, inputs, outputs, and transitions.")
            return

        selected_Connected = [f for f, var in self.connected.items() if var.get()]
        
        # Testing
        print("Number of states:", num_states)
        print("Number of inputs:", num_inputs)
        print("Number of outputs:", num_outputs)
        print("Number of transitions:", num_transition)
        print("Connected:", selected_Connected)


class MainApplication(tk.Tk):
        def __init__(self):
            super().__init__()

            self.frames = {}
            for F in (FSM_Generator,):
                frame = F(self)
                self.frames[F.__name__] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("FSM_Generator")

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

if __name__ == "__main__":
        app = MainApplication()
        app.mainloop()

