import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime

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
        view_order.grid(row=3, column=0, sticky="WEN", rowspan=2, pady=(60, 0), padx=(5, 0))
        exit_program = tk.Button(parent, text="Exit", font=("Arial", 20), command=self.kill_program)
        exit_program.grid(row=6, column=0, sticky="SWEN", padx=(5, 0), pady=(0, 5))
        welcome_label = tk.Label(parent, text=self.coffee_logo_art, font=("Arial", 12), bg="white", justify="left")
        welcome_label.grid(row=0, rowspan=4, column=2, pady=(58, 0), padx=(70, 0))

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
        ViewOrders(view_order_gui_root, create_new_roots)
        view_order_gui_root.mainloop()


class CsvFileUsage:
    def __init__(self):
        self.bean_reg_path = "bean_reg.csv"
        self.customer_data_path = "customer_data.csv"
        self.orders_path = "orders.csv"

    def read_bean_data(self):
        bean_list = []
        with open(self.bean_reg_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                bean_list.append(row)
        return bean_list

    def write_customer_data(self, customer_info):
        with open(self.customer_data_path, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "name", "address", "phone_number", "email", "notes"])
            if file.tell() == 0:  # Check if the file is empty to write the header
                writer.writeheader()
            writer.writerow(customer_info)

    def read_customer_data(self):
        customer_list = []
        with open(self.customer_data_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_list.append(row)
        return customer_list

    def write_orders_data(self, orders_info):
        with open(self.orders_path, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "ID", "order", "cost", "delivery", "address", "notes"])
            if file.tell() == 0:  # Check if the file is empty to write the header
                writer.writeheader()
            writer.writerow(orders_info)


    def read_order_data(self):
        orders_list = []
        with open(self.orders_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                orders_list.append(row)
        return orders_list




class ViewOrders:
    def __init__(self, parent, create_new_roots):
        self.parent = parent
        csv_usage = CsvFileUsage()
        parent.grid_rowconfigure(index=0, weight=1)
        frame = tk.Frame(parent, borderwidth=0, relief="flat", bg="#e0e0e0")
        frame.grid(row=0, column=2, sticky="SWEN")
        parent.grid_columnconfigure(2, weight=1)
        self.create_new_roots = create_new_roots

        # Load order data from CSV
        self.order_data = csv_usage.read_order_data()
        self.customer_data = csv_usage.read_customer_data()
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#e0e0e0", foreground="black", font=("Arial", 11), padding=[0, 5])
        style.configure("Treeview", rowheight=25)


        self.tree = ttk.Treeview(parent, columns=("date", "ID", "order", "cost", "delivery", "address", "notes"))

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.heading("#0", text="")
        self.tree.heading("date", text="Date")
        self.tree.heading("ID", text="ID")
        self.tree.heading("order", text="Order")
        self.tree.heading("cost", text="Cost")
        self.tree.heading("delivery", text="Delivery")
        self.tree.heading("address", text="Address")
        self.tree.heading("notes", text="Notes")

        # Define the column widths
        self.tree.column("date", width=75, anchor="w")
        self.tree.column("ID", width=25, anchor="w")
        self.tree.column("order", width=200, anchor="w")
        self.tree.column("cost", width=50, anchor="w")
        self.tree.column("delivery", width=75, anchor="w")
        self.tree.column("address", width=100, anchor="w")
        self.tree.column("notes", width=150, anchor="w")

        self.tree.bind("<ButtonRelease-1>", self.on_row_click)

        # Insert the customer data into the Treeview
        for order in self.order_data:
            self.tree.insert("", "end", values=(
                order["date"], order["ID"], order["order"], order["cost"], order["delivery"], order["address"],
                order["notes"]))


        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(sticky="NSE", row=0, column=1)
        self.tree.grid(sticky="SWEN", row=0, column=0, rowspan=18)

        # ID Field
        self.id_label = tk.Label(frame, text="ID: ", bg="#e0e0e0", font=("Arial Bold", 12))
        self.id_label.grid(row=0, column=0, sticky="NW")
        self.date_label = tk.Label(frame, text="Date: ", bg="#e0e0e0", font=("Arial Bold", 12))
        self.date_label.grid(row=1, column=0, sticky="NW")


        # Name Field
        self.name_label = tk.Label(frame, text="Name: ", bg="#e0e0e0", font=("Arial, 12"))
        self.name_label.grid(row=2, column=0, sticky="NW")
        self.name_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=2)
        self.name_text.grid(row=3, column=0, sticky="NW", pady=5)

        # Order Field
        self.order_label = tk.Label(frame, text="Order: ", bg="#e0e0e0", font=("Arial, 12"))
        self.order_label.grid(row=4, column=0, sticky="NW")
        self.order_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=4)
        self.order_text.grid(row=5, column=0, sticky="NW", pady=5)

        # Cost Field
        self.cost_label = tk.Label(frame, text="Cost: ", bg="#e0e0e0", font=("Arial, 12"))
        self.cost_label.grid(row=6, column=0, sticky="NW")
        self.cost_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.cost_text.grid(row=7, column=0, sticky="NW", pady=5)

        # Delivery Field
        self.delivery_label = tk.Label(frame, text="Delivery: ", bg="#e0e0e0", font=("Arial, 12"))
        self.delivery_label.grid(row=8, column=0, sticky="NW")
        self.delivery_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.delivery_text.grid(row=9, column=0, sticky="NW", pady=5)

        # Address Field
        self.address_label = tk.Label(frame, text="Address: ", bg="#e0e0e0", font=("Arial, 12"))
        self.address_label.grid(row=10, column=0, sticky="NW")
        self.address_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=2)
        self.address_text.grid(row=11, column=0, sticky="NW", pady=5)

        # Phone Number Field
        self.phone_label = tk.Label(frame, text="Phone Number: ", bg="#e0e0e0", font=("Arial, 12"))
        self.phone_label.grid(row=12, column=0, sticky="NW")
        self.phone_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.phone_text.grid(row=13, column=0, sticky="NW", pady=5)

        # Email Field
        self.email_label = tk.Label(frame, text="Email: ", bg="#e0e0e0", font=("Arial, 12"))
        self.email_label.grid(row=14, column=0, sticky="NW")
        self.email_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.email_text.grid(row=15, column=0, sticky="NW", pady=5)

        # Notes Field
        self.notes_label = tk.Label(frame, text="Notes: ", bg="#e0e0e0", font=("Arial, 12"))
        self.notes_label.grid(row=16, column=0, sticky="NW")
        self.notes_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=3)
        self.notes_text.grid(row=17, column=0, sticky="NW", pady=5)

        self.back_button = tk.Button(frame, text="Back", bg="#ffffff", font=("Arial, 14"), command=self.create_main_menu_root)
        self.back_button.grid(row=18, column=0, sticky="NW", padx=200)

    def on_row_click(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            item = selected_items[0]
            values = self.tree.item(item, "values")
            selected_id = values[1]

            matching_customer = next((customer for customer in self.customer_data if customer["ID"] == selected_id),
                                     None)
            matching_order = next((order for order in self.order_data if order["ID"] == selected_id), None)

            if matching_customer and matching_order:
                # Clears data
                self.id_label.config(text="ID: ")
                self.date_label.config(text="Order: ")
                self.name_text.delete(1.0, tk.END)
                self.order_text.delete(1.0, tk.END)
                self.cost_text.delete(1.0, tk.END)
                self.delivery_text.delete(1.0, tk.END)
                self.address_text.delete(1.0, tk.END)
                self.phone_text.delete(1.0, tk.END)
                self.email_text.delete(1.0, tk.END)
                self.notes_text.delete(1.0, tk.END)

                # Inserts data
                self.id_label.config(text=f"ID: {matching_customer["ID"]}")
                self.date_label.config(text=f"Order:  {matching_order["date"]}")
                self.name_text.insert(1.0, matching_customer["name"])
                self.order_text.insert(1.0, matching_order["order"])
                self.cost_text.insert(1.0, matching_order["cost"])
                self.delivery_text.insert(1.0, matching_order["delivery"])
                self.address_text.insert(1.0, matching_customer["address"])
                self.phone_text.insert(1.0, matching_customer["phone_number"])
                self.email_text.insert(1.0, matching_customer["email"])
                self.notes_text.insert(1.0, matching_order["notes"])

    def create_main_menu_root(self):
        self.parent.destroy()
        main_menu_root = self.create_new_roots.create_main_menu_root()
        MainMenu(main_menu_root, self.create_new_roots)
        main_menu_root.mainloop()

class OrderingGUI:
    def __init__(self, parent, create_new_roots):
        self.parent = parent
        self.create_new_roots = create_new_roots

        self.notebook = ttk.Notebook(parent)
        self.notebook.grid(row=1, column=0, sticky="NSEW")
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure("TNotebook.Tab", padding=[69, 10], font=("Arial", 12))

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
        self.calculated_cost = 0
        self.orders_info = []
        self.order_tree = None
        #       setting RadioButton Style
        self.style = ttk.Style()
        self.style.configure("Custom.TRadiobutton", font=("Arial", 14))

    def frame_config(self, frame): #This is a funcution that configures how my frames are setup, this is used for each frame created

        frame.grid_propagate(False)
        frame.grid_columnconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=70)
        frame.columnconfigure(1, minsize=265)
        frame.columnconfigure(2, minsize=275)
        frame.columnconfigure(3, minsize=265)
        frame.columnconfigure(4, minsize=70)
        total_rows = 8
        row_to_config = {0, 7}
        for row in range(total_rows):
            if row in row_to_config:
                frame.grid_rowconfigure(row, weight=1)
            else:
                frame.grid_rowconfigure(row, weight=0)

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
        self.frame_config(frame)

        #       Delivery Or pickup - this will be a logic gate once I create the database
        pickup_or_delivery_label = tk.Label(frame, text="Pickup or Delivery?:", font=("Arial", 14))
        pickup_or_delivery_label.grid(row=1, column=0, sticky="NW", columnspan=2, padx=5)
        pickup_radio = ttk.Radiobutton(frame, text="Pickup", variable=self.pickup_or_delivery, value="Pickup",
                                       style="Custom.TRadiobutton", takefocus=0)
        pickup_radio.grid(row=1, column=1, sticky="NW", columnspan=2, padx=(100, 0))
        delivery_radio = ttk.Radiobutton(frame, text="Delivery", variable=self.pickup_or_delivery, value="Delivery",
                                         style="Custom.TRadiobutton", takefocus=0)
        delivery_radio.grid(row=1, column=1, sticky="NW", padx=(200, 0), columnspan=2)

        #       Contact details
        name_label = tk.Label(frame, text="Name:", font=("Arial", 14))
        name_label.grid(row=2, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        name_combobox = ttk.Combobox(frame, textvariable=self.name, width=30)
        name_combobox["values"] = ()
        name_combobox.grid(row=2, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        address_label = tk.Label(frame, text="Delivery Address:", font=("Arial", 14))
        address_label.grid(row=3, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        address_combobox = ttk.Combobox(frame, textvariable=self.address, width=30)
        address_combobox["values"] = ()
        address_combobox.grid(row=3, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        phone_number_label = tk.Label(frame, text="Phone Number:", font=("Arial", 14))
        phone_number_label.grid(row=4, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        phone_number_combobox = ttk.Combobox(frame, textvariable=self.phone_number, width=30)
        phone_number_combobox["values"] = ()
        phone_number_combobox.grid(row=4, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        email_label = tk.Label(frame, text="Email Address:", font=("Arial", 14))
        email_label.grid(row=5, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        email_combobox = ttk.Combobox(frame, textvariable=self.email, width=30)
        email_combobox["values"] = ()
        email_combobox.grid(row=5, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        notes_label = tk.Label(frame, text="Notes:", font=("Arial", 14))
        notes_label.grid(row=6, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)
        notes_combobox = ttk.Combobox(frame, textvariable=self.notes, width=30)
        notes_combobox["values"] = ()
        notes_combobox.grid(row=6, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)



        #       Banner navigation buttons
        back_button = tk.Button(frame, text="⌂", font="80", width=7, height=3, command=self.create_main_menu_root)
        back_button.grid(row=8, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3, command=lambda: self.notebook.select(2))
        next_button.grid(row=8, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Customers Details", font=("Arial", 14), fg="white",
                               bg="black")
        current_tab.grid(row=8, column=1, sticky="SNEW", pady=10, columnspan=3)
        banner = tk.Label(frame, bg="black", width=200, height=4)
        banner.grid(row=8, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

    def bean_ordering(self):
        #       Setup the frame for the widgets
        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")

        self.frame_config(frame)

        #       logic gate for which bean is to be ordered
        bean_label = tk.Label(frame, text="Bean type:", font=("Arial", 14))
        bean_label.grid(row=1, column=0, sticky="NW", columnspan=2, padx=5)
        arabica_radio = ttk.Radiobutton(frame, text="Arabica", variable=self.bean, value="Arabica",
                                        style="Custom.TRadiobutton", takefocus=0)
        arabica_radio.grid(row=1, column=1, sticky="NW", columnspan=2, padx=(50, 0))
        robusta_radio = ttk.Radiobutton(frame, text="Robusta", variable=self.bean, value="Robusta",
                                        style="Custom.TRadiobutton", takefocus=0)
        robusta_radio.grid(row=1, column=1, sticky="NW", padx=(150, 0), columnspan=2)
        liberica_radio = ttk.Radiobutton(frame, text="Liberica", variable=self.bean, value="Liberica",
                                         style="Custom.TRadiobutton", takefocus=0)
        liberica_radio.grid(row=1, column=1, sticky="NW", columnspan=2, padx=(250, 0))
        exclesa_radio = ttk.Radiobutton(frame, text="Excelsa", variable=self.bean, value="Excelsa",
                                        style="Custom.TRadiobutton", takefocus=0)
        exclesa_radio.grid(row=1, column=1, sticky="NW", columnspan=2, padx=(350, 0))

        # Bean colour section
        bean_colour_label = tk.Label(frame, text="Bean colour:", font=("Arial", 14))
        bean_colour_label.grid(row=2, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
        light_radio = ttk.Radiobutton(frame, text="Light", variable=self.bean_colour, value="Light",
                                      style="Custom.TRadiobutton", takefocus=0)
        light_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(50, 0))
        medium_radio = ttk.Radiobutton(frame, text="Medium", variable=self.bean_colour, value="Medium",
                                       style="Custom.TRadiobutton", takefocus=0)
        medium_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))
        dark_radio = ttk.Radiobutton(frame, text="Dark", variable=self.bean_colour, value="Dark",
                                     style="Custom.TRadiobutton", takefocus=0)
        dark_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))
        extra_dark_radio = ttk.Radiobutton(frame, text="Extra Dark", variable=self.bean_colour, value="Extra Dark",
                                           style="Custom.TRadiobutton", takefocus=0)
        extra_dark_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(350, 0))

        # Whole or Ground section
        whole_or_ground_label = tk.Label(frame, text="Whole or Ground?:", font=("Arial", 14))
        whole_or_ground_label.grid(row=3, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
        whole_radio = ttk.Radiobutton(frame, text="Whole", variable=self.whole_or_ground, value="Whole",
                                      style="Custom.TRadiobutton", takefocus=0)
        whole_radio.grid(row=3, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))
        ground_radio = ttk.Radiobutton(frame, text="Ground", variable=self.whole_or_ground, value="Ground",
                                       style="Custom.TRadiobutton", takefocus=0)
        ground_radio.grid(row=3, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))

        amount_label = tk.Label(frame, text="Amount:", font=("Arial", 14))
        amount_label.grid(row=4, column=0, sticky="NW", pady=(20, 0), columnspan=2, padx=5)
        amount_spinbox = ttk.Spinbox(frame, from_=0, to=5, textvariable=self.bean_amount, width=30)
        amount_spinbox.grid(row=4, column=1, sticky="NW", pady=(20, 0), padx=(25, 0))

        add_to_order_button = tk.Button(frame, text="+", font=("Arial", 14), command=self.add_to_order)
        add_to_order_button.grid(row=5, column=0, sticky="SWEN")
        add_to_order_label = tk.Label(frame, text="Add to Order", font=("Arial", 14))
        add_to_order_label.grid(row=5, column=1, sticky="SWN", padx=(5, 0))

        #       Banner navigation buttons
        back_button = tk.Button(frame, text="←", font="80", width=7, height=3, command=lambda: self.notebook.select(1))
        back_button.grid(row=8, column=0, sticky="SW")
        next_button = tk.Button(frame, text="→", font="80", width=7, height=3, command=lambda: self.notebook.select(3))
        next_button.grid(row=8, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Bean Ordering", font=("Arial", 14), fg="white", bg="black")
        current_tab.grid(row=8, column=1, sticky="SNEW", pady=10, columnspan=3)
        banner = tk.Label(frame, bg="black", width=200, height=4)
        banner.grid(row=8, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

    def add_to_order(self):
        bean_prices = {"Arabica": 38.50, "Robusta": 38.50, "Liberica": 33.50, "Excelsa": 33.50}
        self.calculated_cost = bean_prices.get(self.bean.get(), 33.50) * self.bean_amount.get() + (
            5 if self.pickup_or_delivery.get() == "Delivery" else 0)

        order_info = {
            "date": f"{datetime.now().strftime('%Y-%m-%d')}",
            "ID": "some_unique_id",
            "order": f"{self.bean.get()} ({self.bean_colour.get()}), {self.whole_or_ground.get()}",
            "cost": f"${self.calculated_cost:.2f}",
            "delivery": self.pickup_or_delivery.get(),
            "address": self.address.get(),
            "notes": self.notes.get()
        }

        self.orders_info.append(order_info)  # Update orders_info
        self.update_treeview()
        self.notebook.select(3)

    def update_treeview(self):
        # Clear the existing items
        self.order_tree.delete(*self.tree.get_children())

        # Insert new items
        for index, row in enumerate(self.orders):
            tag = "oddrow" if index % 2 == 0 else "evenrow"
            self.order_tree.insert("", "end", values=(
            row["date"], row["ID"], row["order"], row["cost"], row["delivery"], row["address"], row["notes"]),
                             tags=(tag,))

    def confirm_order(self):
        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")
        self.frame_config(frame)

        style = ttk.Style()
        style.configure("Treeview.Heading", background="#e0e0e0", foreground="black", font=("Arial", 14),
                        padding=[0, 5])
        style.configure("Treeview", rowheight=25)

        order_label = tk.Label(frame, text="Order Summary:", font=("Arial", 14))
        order_label.grid(row=1, column=0, sticky="NW", columnspan=2)

        self.order_tree = ttk.Treeview(frame, columns=("date", "ID", "order", "cost", "delivery", "address", "notes"),
                                       show="headings", height=5)
        self.order_tree.heading("date", text="Date")
        self.order_tree.heading("ID", text="ID")
        self.order_tree.heading("order", text="Order")
        self.order_tree.heading("cost", text="Cost")
        self.order_tree.heading("delivery", text="Delivery")
        self.order_tree.heading("address", text="Address")
        self.order_tree.heading("notes", text="Notes")

        self.order_tree.column("date", width=100, anchor="center")
        self.order_tree.column("ID", width=100, anchor="center")
        self.order_tree.column("order", width=200, anchor="center")
        self.order_tree.column("cost", width=75, anchor="center")
        self.order_tree.column("delivery", width=100, anchor="center")
        self.order_tree.column("address", width=150, anchor="center")
        self.order_tree.column("notes", width=150, anchor="center")

        for index, row in enumerate(self.orders_info):
            tag = "oddrow" if index % 2 == 0 else "evenrow"
            self.order_tree.insert("", "end", values=(
                row["date"], row["ID"], row["order"], row["cost"], row["delivery"], row["address"], row["notes"]),
                                   tags=(tag,))

        self.order_tree.tag_configure("oddrow", background="#f0f0f0", font=("Arial", 14))
        self.order_tree.tag_configure("evenrow", background="#e0e0e0", font=("Arial", 14))
        self.order_tree.grid(row=2, column=0, sticky="SWEN", columnspan=5)

        add_to_order_button = tk.Button(frame, text="+", font=("Arial", 14), command=lambda: self.notebook.select(2))
        add_to_order_button.grid(row=3, column=0, sticky="SWE")
        add_to_order_label = tk.Label(frame, text="Add to Order", font=("Arial", 14))
        add_to_order_label.grid(row=3, column=1, sticky="NSW", padx=(5, 0))

        cancel_button = tk.Button(frame, text="Cancel Order", font=("Arial", 14), height=2)
        cancel_button.grid(row=7, column=0, columnspan=2, sticky="SW", pady=(0, 10))

        confirm_button = tk.Button(frame, text="Confirm Order", font=("Arial", 14), height=2)
        confirm_button.grid(row=7, column=3, columnspan=2, sticky="SE", pady=(0, 10))

        back_button = tk.Button(frame, text="←", font="80", width=7, height=3, command=lambda: self.notebook.select(2))
        back_button.grid(row=8, column=0, sticky="SW")
        next_button = tk.Button(frame, text="⌂", font="80", width=7, height=3, command=self.create_main_menu_root)
        next_button.grid(row=8, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Confirm Order", font=("Arial", 14), fg="white", bg="black")
        current_tab.grid(row=8, column=1, sticky="SWEN", pady=10, columnspan=3)
        banner = tk.Label(frame, bg="black", width=200, height=4)
        banner.grid(row=8, column=0, columnspan=5, sticky="SWEN")
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
