import tkinter as tk
from tkinter import ttk


class OrderingContentFrames:
    def __init__(self, notebook, create_new_roots):
        self.notebook = notebook
        self.create_new_roots = create_new_roots
        self.pickup = tk.StringVar()
        self.name = tk.StringVar()

    def orderingtab_1(self):
        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        frame.grid_propagate(False)

        pickup_label = tk.Label(frame, text="Pickup or Delivery?:", font=("Arial", 14))
        pickup_label.grid(row=1, column=0, sticky="NW", columnspan=2)
        pickup_radio = tk.Radiobutton(frame, text="Pickup", variable=self.pickup, value="Pickup", font=("Arial", 14))
        pickup_radio.grid(row=1, column=1, sticky="NW", padx=100)
        delivery_radio = tk.Radiobutton(frame, text="Delivery", variable=self.pickup, value="Delivery", font=("Arial", 14))
        delivery_radio.grid(row=1, column=1, sticky="NW", padx=200)

        name_combobox = ttk.Combobox(frame, textvariable=self.name)
        name_combobox['values'] = ()
        name_combobox.grid(row=2, column=0, columnspan=2, sticky="NW")







        back_button = tk.Button(frame, text="←", font="80", width=7, height=3, command=lambda: self.notebook.select(0))
        back_button.grid(row=3, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3, command=lambda: self.notebook.select(2))
        next_button.grid(row=3, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Ordering Tab 1", font="3000", bg="black")
        current_tab.grid(row=3, column=2, sticky="SNEW", pady=10)
        banner = tk.Label(frame, bg="black", width=140, height=4)
        banner.grid(row=3, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

class CreateNewRoots:
    def create_ordering_root(self):
        root = tk.Tk()
        root.geometry("950x660+10+10")
        root.configure(bg="white")
        root.resizable(False, False)
        return root


if __name__ == "__main__":
    root = CreateNewRoots().create_ordering_root()
    notebook = ttk.Notebook(root)
    notebook.grid(row=1, column=0, sticky="NSEW")
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    content_frames = OrderingContentFrames(notebook, CreateNewRoots())
    frame1 = content_frames.orderingtab_1()

    notebook.add(frame1, text="Collection Information")

    root.title("Kahawa Coffee - Ordering Tab 1")
    root.mainloop()
