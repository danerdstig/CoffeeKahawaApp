import tkinter as tk
from tkinter import ttk


class MainMenu:
    def __init__(self, parent, create_new_roots):
        self.parent = parent
        self.create_new_roots = create_new_roots
        parent.grid_rowconfigure(5, weight=1)

        self.coffee_logo_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠒⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡤⠴⠿⠂⠀⠀⠀⠀⠀⣠⠿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠖⠛⠋⠉⠀⠀⠀⠀⠀⢀⣀⣠⠤⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡤⠶⠚⠉⠁⠀⠀⠀⢀⣀⣠⠤⠤⠒⠒⠊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡞⠉⠀⠀⠀⠀⢀⣤⠖⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣷⠇⠀⠀⠀⠀⢯⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠓⠒⠿⠿⣟⡛⠓⠒⠒⠛⢒⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⡤⠦⠴⠾⡿⠒⠛⠛⠛⣳⠿⠷⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣶⠟⠛⠉⠉⠁⠀⢀⣠⠞⠁⠀⣠⡤⠚⠁⠀⠀⠀⠈⠉⠙⠻⢷⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣏⠀⠀⠀⠀⠀⣀⣤⣯⣤⣤⣴⣿⣿⣶⣦⣤⣤⣤⣀⠀⠀⠀⠀⠀⠉⢻⣧⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣄⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣶⣤⡀⠀⢰⣿⡇⣀⣀⡀⠀⠀
⠀⠸⣿⣿⣿⣿⣟⣯⡿⣿⡛⢛⣭⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣟⣦⣼⣿⣿⣿⣷⣿⣿⡟⣉⡉⠙⣧⠀
⠀⠀⢹⣿⣿⣿⡿⢿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠋⠉⠁⣼⡿⠋⠉⠹⡆⢸⡆
⠀⠀⠀⣿⣿⣿⣿⣤⡄⠀⠀⠉⠉⠉⠉⠙⠋⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⢐⡿⠁⠀⠀⢰⡇⣸⠃
⠀⠀⠀⠘⣿⣼⣿⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⣀⡴⠟⣸⠟⠀
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣾⣤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣶⣖⣊⣭⠴⠋⠁⠀⠀
⠀⠀⠀⠀⣀⣨⣿⣿⣿⣿⣿⣶⡔⣡⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣏⡉⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀⣀⣴⠾⠛⠛⠉⣩⣿⣿⣿⢿⣿⣿⣿⣿⣠⣦⣤⣆⣀⣤⣠⣴⣿⣭⡉⠙⠛⢷⣦⠀⠀⠀⠀⠀⠀⠀
⢰⡿⠃⠀⠀⠀⣼⣿⢿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠛⠛⢋⣻⠀⠈⠙⣿⠄⠀⠀⣿⣷⡄⠀⠀⠀⠀⠀
⣿⣧⠲⡀⠀⠀⢿⣿⣏⡉⠉⠉⠉⠙⠛⠒⠺⠖⠒⠛⠋⠉⠉⠀⠀⣰⠟⠀⠀⠀⡎⣻⡇⠀⠀⠀⠀⠀
⠙⠿⣷⣬⣷⢤⣈⡉⠲⠉⣇⠒⠒⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠁⠀⠀⢀⢀⣴⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠈⠛⠻⢿⣶⣭⣿⣶⣤⣤⣤⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⣀⣀⣤⣴⡷⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠿⠿⠛⠿⠟⠛⠛⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """

        welcome_label2 = tk.Label(parent, text="Kahawa Coffee", font=("Arial", 40), bg="white", justify="left")
        welcome_label2.grid(row=2, column=0, sticky="WEN", pady=(5, 0), padx=(5, 0))
        start_order = tk.Button(parent, text="Start Order", font=("Arial", 20), command=self.ordering_root_creation)
        start_order.grid(row=3, column=0, sticky="WEN", padx=(5, 0))
        view_order = tk.Button(parent, text="View Orders", font=("Arial", 20), command=self.view_order_root_creation)
        view_order.grid(row=3, column=0, sticky="WEN", rowspan=2, pady=(60,0), padx=(5, 0))
        exit_program = tk.Button(parent, text="Exit", font=("Arial", 20), command=self.kill_program)
        exit_program.grid(row=6, column=0, sticky="SWEN", padx=(5, 0), pady=(0, 5))
        welcome_label = tk.Label(parent, text=self.coffee_logo_art, font=("Arial", 12), bg="white", justify="left")
        welcome_label.grid(row=0, rowspan=4, column=2, pady=(58, 0), padx=(70,0))

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
        self.pickup_or_delivery = tk.StringVar(value="N/A")
        self.name = tk.StringVar(value="")
        self.address = tk.StringVar(value="")
        self.phone_number = tk.StringVar(value="")
        self.notes = tk.StringVar(value="")
        self.email = tk.StringVar(value="")
        self.bean = tk.StringVar(value="N/A")
        self.whole_or_ground = tk.StringVar(value="N/A")
        self.bean_colour = tk.StringVar(value="N/A")
        self.bean_amount = tk.IntVar()

#       setting RadioButton Style
        self.style = ttk.Style()
        self.style.configure("Custom.TRadiobutton", font=("Arial", 14))

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
        pickup_or_delivery_label = tk.Label(frame, text="Pickup or Delivery?:", font=("Arial", 14))
        pickup_or_delivery_label.grid(row=0, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
        pickup_radio = ttk.Radiobutton(frame, text="Pickup", variable=self.pickup_or_delivery, value="Pickup", style="Custom.TRadiobutton", takefocus=0)
        pickup_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(100, 0))
        delivery_radio = ttk.Radiobutton(frame, text="Delivery", variable=self.pickup_or_delivery, value="Delivery", style="Custom.TRadiobutton", takefocus=0)
        delivery_radio.grid(row=0, column=1, sticky="NW", pady=(20, 0), padx=(200, 0),  columnspan=2)

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
        bean_label.grid(row=0, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
        arabica_radio = ttk.Radiobutton(frame, text="Arabica", variable=self.bean, value="Arabica", style="Custom.TRadiobutton", takefocus=0)
        arabica_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(50, 0))
        robusta_radio = ttk.Radiobutton(frame, text="Robusta", variable=self.bean, value="Robusta", style="Custom.TRadiobutton", takefocus=0)
        robusta_radio.grid(row=0, column=1, sticky="NW", pady=(20, 0), padx=(150, 0),  columnspan=2)
        liberica_radio = ttk.Radiobutton(frame, text="Liberica", variable=self.bean, value="Liberica", style="Custom.TRadiobutton", takefocus=0)
        liberica_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))
        exclesa_radio = ttk.Radiobutton(frame, text="Excelsa", variable=self.bean, value="Excelsa", style="Custom.TRadiobutton", takefocus=0)
        exclesa_radio.grid(row=0, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(350, 0))

        # Bean colour section
        bean_colour_label = tk.Label(frame, text="Bean colour:", font=("Arial", 14))
        bean_colour_label.grid(row=1, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
        light_radio = ttk.Radiobutton(frame, text="Light", variable=self.bean_colour, value="Light", style="Custom.TRadiobutton", takefocus=0)
        light_radio.grid(row=1, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(50, 0))
        medium_radio = ttk.Radiobutton(frame, text="Medium", variable=self.bean_colour, value="Medium", style="Custom.TRadiobutton", takefocus=0)
        medium_radio.grid(row=1, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))
        dark_radio = ttk.Radiobutton(frame, text="Dark", variable=self.bean_colour, value="Dark", style="Custom.TRadiobutton", takefocus=0)
        dark_radio.grid(row=1, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))
        extra_dark_radio = ttk.Radiobutton(frame, text="Extra Dark", variable=self.bean_colour, value="Extra Dark", style="Custom.TRadiobutton", takefocus=0)
        extra_dark_radio.grid(row=1, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(350, 0))

        # Whole or Ground section
        whole_or_ground_label = tk.Label(frame, text="Whole or Ground?:", font=("Arial", 14))
        whole_or_ground_label.grid(row=2, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
        whole_radio = ttk.Radiobutton(frame, text="Whole", variable=self.whole_or_ground, value="Whole", style="Custom.TRadiobutton", takefocus=0)
        whole_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))
        ground_radio = ttk.Radiobutton(frame, text="Ground", variable=self.whole_or_ground, value="Ground", style="Custom.TRadiobutton", takefocus=0)
        ground_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))

        amount_label = tk.Label(frame, text="Amount:", font=("Arial", 14))
        amount_label.grid(row=3, column=0, sticky="NW", pady=(20, 0), columnspan=2, padx=5)
        amount_spinbox = ttk.Spinbox(frame, from_=0, to=5, textvariable=self.bean_amount, width=30)
        amount_spinbox.grid(row=3, column=1, sticky="NW", pady=(20, 0),  padx=(25, 0))

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

        style = ttk.Style()
        style.configure("Treeview.Heading", background="#f0f0f0", foreground="black")

        order_tree = ttk.Treeview(frame, columns=("Bean", "Type", "Price"), show="headings")
        order_tree.heading("Bean", text="Bean")
        order_tree.heading("Type", text="Type")
        order_tree.heading("Price", text="Price")
        order_tree.column("Bean", width=100, anchor="center")
        order_tree.column("Type", width=100, anchor="center")
        order_tree.column("Price", width=100, anchor="center")
        data = [
            ("Arabica", "Whole Bean", "$15.00"),
            ("Robusta", "Ground", "$12.50"),
            ("Liberica", "Espresso", "$18.00")
        ]
        for index, row in enumerate(data):
            tag = 'oddrow' if index % 2 == 0 else 'evenrow'
            order_tree.insert("", "end", values=row, tags=(tag,))
        
        order_tree.tag_configure('oddrow', background='#f0f0f0')
        order_tree.tag_configure('evenrow', background='#e0e0e0')
            
        order_tree.grid(row=1, column=1, sticky="NSWE")


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
        root.geometry("950x660+300+300")
        root.configure(bg="white")
        root.title("Kahawa Coffee™")
        root.resizable(False, False)
        return root

    def create_view_order_root(self):
        root = tk.Tk()
        root.geometry("950x660+300+300")
        root.configure(bg="white")
        root.title("Kahawa Coffee™")
        root.resizable(False, False)
        return root

    def create_main_menu_root(self):
        root = tk.Tk()
        root.geometry("950x660+300+300")
        root.configure(bg="white")
        root.title("Kahawa Coffee™")
        root.resizable(False, False)
        return root


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("950x660+300+300")
    root.configure(bg="white")
    root.title("Kahawa Coffee™")
    root.resizable(False, False)
    create_new_roots = CreateNewRoots()
    app = MainMenu(root, create_new_roots)
    root.mainloop()
