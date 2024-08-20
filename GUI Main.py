import tkinter as tk
from tkinter import ttk


class MainMenu:
    def __init__(self, parent, create_new_roots):
        self.parent = parent
        self.create_new_roots = create_new_roots
        parent.rowconfigure(0, minsize=110, weight=1)
        parent.rowconfigure(1, minsize=110, weight=1)
        parent.rowconfigure(2, minsize=110, weight=1)
        parent.rowconfigure(3, minsize=110, weight=1)
        parent.rowconfigure(4, minsize=110, weight=1)
        parent.grid_columnconfigure(0, minsize=60, weight=1)
        parent.grid_columnconfigure(1, minsize=350, weight=1)
        parent.grid_columnconfigure(2, minsize=125, weight=1)
        parent.grid_columnconfigure(3, minsize=350, weight=1)
        parent.grid_columnconfigure(4, minsize=60, weight=1)

        welcome_label = tk.Label(parent, text="Kahawa Coffee", font="Arial, 40", bg="white")
        welcome_label.grid(row=2, column=1, columnspan=3, sticky="N")
        start_order = tk.Button(parent, text="Start Order", font="Arial, 20", command=self.ordering_root_creation)
        start_order.grid(row=3, column=3, sticky="WN", pady=10)
        view_order = tk.Button(parent, text="View Orders", font="Arial, 20", command=self.view_order_root_creation)
        view_order.grid(row=3, column=1, sticky="EN", pady=10)
        exit_program = tk.Button(parent, text="Exit", font="Arial, 20", height=1, command=self.kill_program)
        exit_program.grid(row=4, column=2, sticky="SWEN")
#        back_button = tk.Button(parent, text="←", font="80", width=7, height=3)
#        back_button.grid(row=0, column=0, sticky="SW")
#        next_button = tk.Button(parent, text="→", font="80", width=7, height=3, command=self.switch_to_ordering_gui)
#        next_button.grid(row=0, column=4, sticky="SW")

#        self.photo_welcome_image = tk.PhotoImage(file="Kahawa Coffee tiny.png")
#        self.photo_welcome = tk.Label(parent, image=self.photo_welcome_image, bd=0)
#        self.photo_welcome.grid(row=0, column=2, sticky="S")

        banner = tk.Label(parent, bg="black", width=200, height=4)
        banner.grid(row=5, column=0, columnspan=5, sticky="SWE")
        banner.lower()

    def kill_program(self):
        self.parent.destroy()

    def ordering_root_creation(self):
        self.parent.destroy()
        ordering_gui_root = self.create_new_roots.create_ordering_root()
        OrderingGUI(ordering_gui_root, self.create_new_roots)
        ordering_gui_root.mainloop()

    def view_order_root_creation(self):
        self.parent.destroy()
        view_order_gui_root = self.create_new_roots.create_view_order_root()
        view_order_gui_root.mainloop()
        print("worked")
#        ViewOrdersGUI(self.parent)


class OrderingGUI:
    def __init__(self, parent, create_new_roots):
        self.parent = parent
        self.create_new_roots = create_new_roots

        self.notebook = ttk.Notebook(parent)
        self.notebook.grid(row=1, column=0, sticky="NSEW")
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure("TNotebook.Tab", padding=[20, 10], font=("Arial", 12))

        content_frames = OrderingContentFrames(self.notebook, parent, self.create_new_roots)
        frame0 = content_frames.main_menu()
        frame1 = content_frames.customer_details()
        frame2 = content_frames.bean_ordering()
        frame3 = content_frames.confirm_order()

        self.notebook.add(frame0, text="⌂")
        self.notebook.add(frame1, text="Collection Information")
        self.notebook.add(frame2, text="Bean Ordering")
        self.notebook.add(frame3, text="Shopping Cart")

        self.notebook.select(1)
        self.notebook.bind("<<NotebookTabChanged>>", self.main_menu_click)

    def main_menu_click(self, event):
        selected_tab = self.notebook.index(self.notebook.select())
        if selected_tab == 0:
            self.create_main_menu_root()

    def create_main_menu_root(self):
        self.parent.destroy()
        main_menu_root = self.create_new_roots.create_main_menu_root()
        MainMenu(main_menu_root, self.create_new_roots)
        main_menu_root.mainloop()


class OrderingContentFrames:
    def __init__(self, notebook, parent, create_new_roots):
        self.notebook = notebook
        self.parent = parent
        self.create_new_roots = create_new_roots
        self.pickup = tk.StringVar(value="")
        self.name = tk.StringVar(value="")
        self.address = tk.StringVar(value="")
        self.phone_number = tk.StringVar(value="")
        self.notes = tk.StringVar(value="")
        self.email = tk.StringVar(value="")
        self.bean = tk.StringVar(value="")
    def main_menu(self):
        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")
        return frame

    def create_main_menu_root(self):
        self.parent.destroy()
        main_menu_root = self.create_new_roots.create_main_menu_root()
        MainMenu(main_menu_root, self.create_new_roots)
        main_menu_root.mainloop()

    def customer_details(self):

#       Setup the frame for the widgets
        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")

        frame.grid_rowconfigure(6, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        frame.grid_propagate(False)

#       Delivery Or pickup - this will be a logic gate once I create the database
        pickup_label = tk.Label(frame, text="Pickup or Delivery?:", font=("Arial", 14))
        pickup_label.grid(row=0, column=0, sticky="NW", columnspan=2, pady=20)
        pickup_radio = tk.Radiobutton(frame, text="Pickup", variable=self.pickup, value="Pickup", font=("Arial", 14))
        pickup_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=20, padx=(100, 0))
        delivery_radio = tk.Radiobutton(frame, text="Delivery", variable=self.pickup, value="Delivery", font=("Arial", 14))
        delivery_radio.grid(row=0, column=1, sticky="NW", pady=20, padx=(200, 0),  columnspan=2)

#       Contact details
        name_label = tk.Label(frame, text="Name:", font=("Arial", 14))
        name_label.grid(row=1, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        name_combobox = ttk.Combobox(frame, textvariable=self.name, width=30)
        name_combobox['values'] = ()
        name_combobox.grid(row=1, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        address_label = tk.Label(frame, text="Delivery Address:", font=("Arial", 14))
        address_label.grid(row=2, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        address_combobox = ttk.Combobox(frame, textvariable=self.address, width=30)
        address_combobox['values'] = ()
        address_combobox.grid(row=2, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        phone_number_label = tk.Label(frame, text="Phone Number:", font=("Arial", 14))
        phone_number_label.grid(row=3, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        phone_number_combobox = ttk.Combobox(frame, textvariable=self.phone_number, width=30)
        phone_number_combobox['values'] = ()
        phone_number_combobox.grid(row=3, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        email_label = tk.Label(frame, text="Email Address:", font=("Arial", 14))
        email_label.grid(row=4, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        email_combobox = ttk.Combobox(frame, textvariable=self.email, width=30)
        email_combobox['values'] = ()
        email_combobox.grid(row=4, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        notes_label = tk.Label(frame, text="Notes:", font=("Arial", 14))
        notes_label.grid(row=5, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        notes_combobox = ttk.Combobox(frame, textvariable=self.notes, width=30)
        notes_combobox['values'] = ()
        notes_combobox.grid(row=5, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

#       Banner navigation buttons
        back_button = tk.Button(frame, text="⌂", font="80", width=7, height=3, command=self.create_main_menu_root)
        back_button.grid(row=7, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3, command=lambda: self.notebook.select(2))
        next_button.grid(row=7, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Customers Details", font=("Arial", 14), fg="white", bg="black")
        current_tab.grid(row=7, column=1, sticky="SNEW", pady=10, columnspan=3)
        banner = tk.Label(frame, bg="black", width=200, height=4)
        banner.grid(row=7, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

    def bean_ordering(self):
#       Setup the frame for the widgets
        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")

        frame.grid_rowconfigure(6, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        frame.grid_propagate(False)

#       logic gate for which bean is to be ordered
        bean_label = tk.Label(frame, text="Bean type:", font=("Arial", 14))
        bean_label.grid(row=0, column=0, sticky="NW", columnspan=2, pady=20)
        arabica_radio = tk.Radiobutton(frame, text="Arabica", variable=self.bean, value="Arabica", font=("Arial", 14))
        arabica_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=20, padx=(25, 0))
        robusta_radio = tk.Radiobutton(frame, text="Robusta", variable=self.bean, value="Robusta", font=("Arial", 14))
        robusta_radio.grid(row=0, column=1, sticky="NW", pady=20, padx=(125, 0),  columnspan=2)
        liberica_radio = tk.Radiobutton(frame, text="Liberica", variable=self.bean, value="Liberica", font=("Arial", 14))
        liberica_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=20, padx=(225, 0))
        exclesa_radio = tk.Radiobutton(frame, text="Excelsa", variable=self.bean, value="Excelsa", font=("Arial", 14))
        exclesa_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=20, padx=(325, 0))

#       Banner navigation buttons
        back_button = tk.Button(frame, text="←", font="80", width=7, height=3, command=lambda: self.notebook.select(1))
        back_button.grid(row=7, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3, command=lambda: self.notebook.select(3))
        next_button.grid(row=7, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Bean Ordering", font=("Arial", 14), fg="white", bg="black")
        current_tab.grid(row=7, column=1, sticky="SNEW", pady=10, columnspan=3)
        banner = tk.Label(frame, bg="black", width=200, height=4)
        banner.grid(row=7, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

    def confirm_order(self):
        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        frame.grid_propagate(False)

        back_button = tk.Button(frame, text="←", font="80", width=7, height=3, command=lambda: self.notebook.select(2))
        back_button.grid(row=3, column=0, sticky="SW")
        next_button = tk.Button(frame, text="⌂", font="80", width=7, height=3, command=self.create_main_menu_root)
        next_button.grid(row=3, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Confirm Order", font=("Arial", 14), fg="white", bg="black")
        current_tab.grid(row=7, column=1, sticky="SNEW", pady=10, columnspan=3)
        banner = tk.Label(frame, bg="black", width=200, height=4)
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

    def create_view_order_root(self):
        root = tk.Tk()
        root.geometry("950x660+10+10")
        root.configure(bg="white")
        root.resizable(False, False)
        return root

    def create_main_menu_root(self):
        root = tk.Tk()
        root.geometry("950x660+10+10")
        root.configure(bg="white")
        root.resizable(False, False)
        return root


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("950x660+10+10")
    root.configure(bg="white")
    root.resizable(False, False)
    create_new_roots = CreateNewRoots()
    app = MainMenu(root, create_new_roots)
    root.title("Kahawa Coffee")
    root.mainloop()
