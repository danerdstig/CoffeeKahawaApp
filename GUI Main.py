import tkinter as tk
from tkinter import ttk


class MainMenu:
    def __init__(self):
        print("hi")


class OrderingGUI:
    def __init__(self, parent):
        self.parent = parent

        self.notebook = ttk.Notebook(parent)
        self.notebook.grid(row=1, column=0, sticky='NSEW')
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10], font=('Arial', 12))

        content_frames = ContentFrames(self.notebook)
        frame = ttk.Frame(self.notebook)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=60, weight=1)
        frame.columnconfigure(1, minsize=275, weight=1)
        frame.columnconfigure(2, minsize=275, weight=1)
        frame.columnconfigure(3, minsize=275, weight=1)
        frame.columnconfigure(4, minsize=60, weight=1)
        frame1 = content_frames.this_is_a_test()
        frame2 = content_frames.orderingtab_1()
        frame3 = content_frames.orderingtab_2()

        self.notebook.add(frame1, text='Collection Information')
        self.notebook.add(frame2, text='Bean Ordering')
        self.notebook.add(frame3, text='Shopping Cart')


class ContentFrames:
    def __init__(self, notebook):
        self.notebook = notebook

    def this_is_a_test(self):
        frame = ttk.Frame(self.notebook, borderwidth=0, relief='flat')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        frame.grid_propagate(False)

        label1 = tk.Label(frame, background="#000000", foreground="#ffffff", padx=30, pady=30,
                          text="THIS IS A TEST", font=("Times", 24, "bold"))
        label1.grid(row=0, column=0, sticky="NSEW", rowspan=5)

# --------------------- menu buttons copy paste
        back_button = tk.Button(frame, text="←", font="80", width=7, height=3)
        back_button.grid(row=3, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3, command=orderingtab_1)
        next_button.grid(row=3, column=4, sticky="SW")
        current_tab = tk.Label(frame, text='Kahawa Coffee™ - Ordering Tab 1', font="3000", bg='light gray')
        current_tab.grid(row=3, column=2, sticky="SNEW", pady=10)
        banner = tk.Label(frame, bg='light gray', width=200, height=4)
        banner.grid(row=3, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

    def orderingtab_1(self):
        frame = ttk.Frame(self.notebook, borderwidth=0, relief='flat')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        frame.grid_propagate(False)

        label = ttk.Label(frame, text='Tab 2')
        label.grid(row=0, column=1, sticky="NSEW", pady=10)
        entry = ttk.Entry(frame)
        entry.grid(row=1, column=1, sticky="NSEW", pady=5)
        button = ttk.Button(frame, text="Submit")
        button.grid(row=2, column=2, sticky="NSEW", pady=5)
#        text = tk.Text(frame, height=10, width=40)
#        text.grid(row=3, column=3, sticky="NSEW", pady=5)

# --------------------- menu buttons copy paste
        back_button = tk.Button(frame, text="←", font="80", width=7, height=3)
        back_button.grid(row=3, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3)
        next_button.grid(row=3, column=4, sticky="SW")
        current_tab = tk.Label(frame, text='Kahawa Coffee™ - Ordering Tab 1', font="3000", bg='light gray')
        current_tab.grid(row=3, column=2, sticky="SNEW", pady=10)
        banner = tk.Label(frame, bg='light gray', width=200, height=4)
        banner.grid(row=3, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

    def orderingtab_2(self):
        frame = ttk.Frame(self.notebook, borderwidth=0, relief='flat')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        frame.grid_propagate(False)

# --------------------- menu buttons copy paste
        back_button = tk.Button(frame, text="←", font="80", width=7, height=3)
        back_button.grid(row=3, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3)
        next_button.grid(row=3, column=4, sticky="SW")
        current_tab = tk.Label(frame, text='Kahawa Coffee™ - Ordering Tab 2', font="3000", bg='light gray')
        current_tab.grid(row=3, column=2, sticky="SNEW", pady=10)
        banner = tk.Label(frame, bg='light gray', width=200, height=4)
        banner.grid(row=3, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("950x660")
#    root.overrideredirect(True)
    root.configure(bg='white')
    root.resizable(False, False)
    app = OrderingGUI(root)
    root.title("Kahawa Coffee")
    root.mainloop()
