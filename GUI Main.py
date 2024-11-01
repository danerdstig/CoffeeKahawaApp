import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime
from dataclasses import dataclass, field


'''
 Essentially, each of the first 5 classes manage and create different 
 windows and components of the program, Hence why they're named after the window they manage.
 Also, PyCharm is getting angry at me for breaking the PEP-8 character line length limit with these comments whoops.
'''


class MainMenu:  # Main menu window

    def __init__(self, parent, create_new_roots):
        self.parent = parent
        self.create_new_roots = create_new_roots
        parent.grid_rowconfigure(5, weight=1)  # configures the grid layout so that the coffee logo art is centred in the middle of the screen vertically

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

        kahawa_coffee_label = tk.Label(parent, text="Kahawa Coffee", font=("Arial", 40), bg="white", justify="left")
        kahawa_coffee_label.grid(row=2, column=0, sticky="WEN", pady=(5, 0), padx=(5, 0))

        start_order_button = tk.Button(parent, text="Start Order", font=("Arial", 20), command=self.ordering_root_creation)
        start_order_button.grid(row=3, column=0, sticky="WEN", padx=(5, 0))

        view_order_button = tk.Button(parent, text="View Orders", font=("Arial", 20), command=self.view_order_root_creation)
        view_order_button.grid(row=3, column=0, sticky="WEN", rowspan=2, pady=(60, 0), padx=(5, 0))

        exit_program_button = tk.Button(parent, text="Exit", font=("Arial", 20), command=self.kill_program)
        exit_program_button.grid(row=6, column=0, sticky="SWEN", padx=(5, 0), pady=(0, 5))

        coffee_art_label = tk.Label(parent, text=self.coffee_logo_art, font=("Arial", 12), bg="white", justify="left")
        coffee_art_label.grid(row=0, rowspan=4, column=2, pady=(58, 0), padx=(70, 0))

    def kill_program(self):  # this could be a lambda func but I can't be bothered changing it to one now
        self.parent.destroy()

    def ordering_root_creation(self):  # creates the ordering root window
        self.parent.destroy()
        ordering_gui_root = self.create_new_roots.create_root()
        OrderingGUI(ordering_gui_root, self.create_new_roots)  # calls class to populate the ordering window
        ordering_gui_root.mainloop()  # creates the window

    def view_order_root_creation(self):  # creates the view orders root window
        self.parent.destroy()
        view_order_gui_root = self.create_new_roots.create_root()
        ViewOrders(view_order_gui_root, create_new_roots) # calls class to populate the view orders window
        view_order_gui_root.mainloop()  # creates the window


class CsvFileUsage:  #handles use of Csv Files throughout the code
    def __init__(self):
        self.bean_reg_path = "bean_reg.csv"  # registering file locations
        self.customer_data_path = "customer_data.csv"  # registering file locations
        self.orders_path = "orders.csv"  # registering file locations

    def read_bean_data(self):  # Reads bean data and converts it into a list for the program to use
        bean_list = []
        with open(self.bean_reg_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                bean_list.append(row)
        return bean_list  # reads every row of the csv and converts it into a list, [(Arabica, 38.50),(Excelsa, 33.50)] etc

    def read_customer_data(self):  # Reads customer data to display in the view orders window
        customer_list = []
        with open(self.customer_data_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_list.append(row)
        return customer_list  # reads every row of the csv and converts it into a single list entry list,
        # [(ID, name, phone number, email, address, notes)] etc this means that later on it is
        # easily to split these data points when trying to split in the view orders window

    def read_order_data(self):  # Reads order data to display in the view orders window
        orders_list = []
        with open(self.orders_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                orders_list.append(row)
        return orders_list  # reads every row of the csv and converts it into a single list entry list,
        # [(date, ID, order, cost, delivery, address, notes)] etc this means that later on it is
        # easily to split these data points when trying to split in the view orders window

    def write_customer_data(self, customer_info):  # used to write new information to the Csv file
        with open(self.customer_data_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(customer_info.values())  # each column is separated by a
            # comma meaning the csv files are formatted as so:
            '''
            "ID": data,
            "name": data,
            "phone number": data,
            "email": data,
            "address": data,
            "notes": data
            '''


    def write_order_data(self, order_info):# used to write new information to the Csv file
        with open(self.orders_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            print(order_info.values())
            writer.writerow(order_info.values())# each column is separated by a
            # comma meaning the csv files are formatted as so:
            '''
            "date": data,
            "ID": data,
            "order": data,
            "cost" data,
            "delivery": data,
            "address": data,
            "notes": data
            '''

    def get_next_id(self): # simple script to calculate what the current ID number is.
        # Takes the rows in the customer data and counts each row to find the next ID available.
        last_id = 1
        with open(self.customer_data_path, mode='r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                last_id += 1
        return last_id + 1


class ViewOrders:  # handles the view orders window
    def __init__(self, parent, create_new_roots):
        self.parent = parent
        csv_usage = CsvFileUsage()
        parent.grid_rowconfigure(index=0, weight=1)  # row 1 needs a weight so that it keeps the correct
        # sizing so that the Label of each column are visible
        frame = tk.Frame(parent, borderwidth=0, relief="flat", bg="#e0e0e0")
        frame.grid(row=0, column=2, sticky="SWEN")
        parent.grid_columnconfigure(2, weight=1)
        self.create_new_roots = create_new_roots

        # Load order data from CSV
        self.order_data = csv_usage.read_order_data()
        self.customer_data = csv_usage.read_customer_data()
        style = ttk.Style()  # tweaking treeview look and size
        style.configure("Treeview.Heading", background="#e0e0e0", foreground="black", font=("Arial", 11), padding=[0, 5])
        style.configure("Treeview", rowheight=25)

        self.tree = ttk.Treeview(parent, columns=("date", "ID", "order", "cost", "delivery", "address", "notes"))

        self.tree.column("#0", width=0, stretch=tk.NO)  # these two lines format my treeview so that it's the correct
        self.tree.heading("#0", text="")                # height and width. It also means there's no blank column at the start.
        self.tree.heading("date", text="Date")
        self.tree.heading("ID", text="ID")
        self.tree.heading("order", text="Order")
        self.tree.heading("cost", text="Cost")
        self.tree.heading("delivery", text="Delivery")
        self.tree.heading("address", text="Address")
        self.tree.heading("notes", text="Notes")

        self.tree.column("date", width=75, anchor="w")         # Define the column widths so that information
        self.tree.column("ID", width=25, anchor="w")           # is appropriately displayed.
        self.tree.column("order", width=200, anchor="w")
        self.tree.column("cost", width=50, anchor="w")
        self.tree.column("delivery", width=75, anchor="w")
        self.tree.column("address", width=100, anchor="w")
        self.tree.column("notes", width=150, anchor="w")

        self.tree.bind("<ButtonRelease-1>", self.on_row_click)  # setups the detailed data click.

        for order in self.order_data:         # Insert the customer data into the Treeview from the order csv.
            self.tree.insert("", "end", values=(
                order["date"], order["ID"], order["order"], order["cost"], order["delivery"], order["address"],
                order["notes"]))

        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.tree.yview)  # scrollbar to view more information.
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(sticky="NSE", row=0, column=1)
        self.tree.grid(sticky="SWEN", row=0, column=0, rowspan=18)

        # setup for the more detailed view on the right of the screen,
        # labels used for titles, text for the information boxes.

        self.id_label = tk.Label(frame, text="ID: ", bg="#e0e0e0", font=("Arial Bold", 12))
        self.id_label.grid(row=0, column=0, sticky="NW")
        self.date_label = tk.Label(frame, text="Date: ", bg="#e0e0e0", font=("Arial Bold", 12))
        self.date_label.grid(row=1, column=0, sticky="NW")

        self.name_label = tk.Label(frame, text="Name: ", bg="#e0e0e0", font=("Arial, 12"))
        self.name_label.grid(row=2, column=0, sticky="NW")
        self.name_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=2)
        self.name_text.grid(row=3, column=0, sticky="NW", pady=5)

        self.order_label = tk.Label(frame, text="Order: ", bg="#e0e0e0", font=("Arial, 12"))
        self.order_label.grid(row=4, column=0, sticky="NW")
        self.order_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=4)
        self.order_text.grid(row=5, column=0, sticky="NW", pady=5)

        self.cost_label = tk.Label(frame, text="Cost: ", bg="#e0e0e0", font=("Arial, 12"))
        self.cost_label.grid(row=6, column=0, sticky="NW")
        self.cost_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.cost_text.grid(row=7, column=0, sticky="NW", pady=5)

        self.delivery_label = tk.Label(frame, text="Delivery: ", bg="#e0e0e0", font=("Arial, 12"))
        self.delivery_label.grid(row=8, column=0, sticky="NW")
        self.delivery_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.delivery_text.grid(row=9, column=0, sticky="NW", pady=5)

        self.address_label = tk.Label(frame, text="Address: ", bg="#e0e0e0", font=("Arial, 12"))
        self.address_label.grid(row=10, column=0, sticky="NW")
        self.address_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=2)
        self.address_text.grid(row=11, column=0, sticky="NW", pady=5)

        self.phone_label = tk.Label(frame, text="Phone Number: ", bg="#e0e0e0", font=("Arial, 12"))
        self.phone_label.grid(row=12, column=0, sticky="NW")
        self.phone_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.phone_text.grid(row=13, column=0, sticky="NW", pady=5)

        self.email_label = tk.Label(frame, text="Email: ", bg="#e0e0e0", font=("Arial, 12"))
        self.email_label.grid(row=14, column=0, sticky="NW")
        self.email_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=1)
        self.email_text.grid(row=15, column=0, sticky="NW", pady=5)

        self.notes_label = tk.Label(frame, text="Notes: ", bg="#e0e0e0", font=("Arial, 12"))
        self.notes_label.grid(row=16, column=0, sticky="NW")
        self.notes_text = tk.Text(frame, bg="#ffffff", font=("Arial, 12"), height=3)
        self.notes_text.grid(row=17, column=0, sticky="NW", pady=5)

        self.back_button = tk.Button(frame, text="Back", bg="#ffffff", font=("Arial, 14"), command=self.create_root)
        self.back_button.grid(row=18, column=0, sticky="NW", padx=200)  # escape view orders window

        most_recent_order = len(self.order_data) - 1  # This figures out when you make an order which order
        # it was so that it can show you the information when you are on the view orders window.
        self.tree.selection_set(self.tree.get_children()[most_recent_order])
        self.tree.focus(self.tree.get_children()[most_recent_order])

        self.on_row_click()  # to activate the detailed view of your most recent order without the click.

    def on_row_click(self, event=None):  # when a row is clicked it'll show a full detailed view of the order,
        # event=None is needed for the case when no click is used to chane the focus of the view.

        selected_items = self.tree.selection()
        if not selected_items:  # When no row is clicked, take the default row
            selected_items = [self.tree.focus()]
        if selected_items:
            item = selected_items[0]
            values = self.tree.item(item, "values") # takes the values and puts it into the text widgets
            selected_id = values[1]

            matching_customer = next((customer for customer in self.customer_data if customer["ID"] == selected_id),
                                     None)
            matching_order = next((order for order in self.order_data if order["ID"] == selected_id), None) # This links
            # up the ID of the two different sheets so the correct information can be displayed to the user.

            if matching_customer and matching_order:
                self.id_label.config(text="ID: ")
                self.date_label.config(text="Order: ")
                self.name_text.delete(1.0, tk.END)
                self.order_text.delete(1.0, tk.END)
                self.cost_text.delete(1.0, tk.END)
                self.delivery_text.delete(1.0, tk.END)
                self.address_text.delete(1.0, tk.END)
                self.phone_text.delete(1.0, tk.END)
                self.email_text.delete(1.0, tk.END)
                self.notes_text.delete(1.0, tk.END) # resets data

                self.id_label.config(text=f"ID: {matching_customer["ID"]}")
                self.date_label.config(text=f"Order:  {matching_order["date"]}")
                self.name_text.insert(1.0, matching_customer["name"])
                self.order_text.insert(1.0, matching_order["order"])
                self.cost_text.insert(1.0, matching_order["cost"])
                self.delivery_text.insert(1.0, matching_order["delivery"])
                self.address_text.insert(1.0, matching_customer["address"])
                self.phone_text.insert(1.0, matching_customer["phone_number"])
                self.email_text.insert(1.0, matching_customer["email"])
                self.notes_text.insert(1.0, matching_order["notes"])  # Inserts new data

    def create_root(self):  # when the back button is pressed it calls this to bring you back to the main menu.
        self.parent.destroy()
        main_menu_root = self.create_new_roots.create_root()
        MainMenu(main_menu_root, self.create_new_roots)
        main_menu_root.mainloop()


class OrderingGUI:  # coffee bean ordering window
    def __init__(self, parent, create_new_roots):
        self.parent = parent
        self.create_new_roots = create_new_roots
        self.csvfile = CsvFileUsage()
        self.notebook = ttk.Notebook(parent)  # notebook is used to have a 'progress bar' convention.
        self.notebook.grid(row=1, column=0, sticky="NSEW")


        parent.grid_rowconfigure(1, weight=1)  # configures row and column so that the
        parent.grid_columnconfigure(0, weight=1)  # notebook will fill the entire window.

        style = ttk.Style()  # adjusting the notebook 'tabs'
        style.configure("TNotebook.Tab", padding=[69, 10], font=("Arial", 12))  # tabs now fill the width of the screen.

        content_frames = ContentFrames(self.notebook, parent, self.create_new_roots)  # frames used by the notebook to show information.
        frame0 = content_frames.main_menu()  # this is a placeholder frame so that I can run a funcution when this frame is called.
        frame1 = content_frames.customer_details_tab()
        frame2 = content_frames.bean_ordering_tab()
        frame3 = content_frames.confirm_order_tab()

        self.notebook.add(frame0, text="⌂")
        self.notebook.add(frame1, text="Collection Information")
        self.notebook.add(frame2, text="Bean Ordering")
        self.notebook.add(frame3, text="Shopping Cart")  # adding tab titles.

        self.notebook.select(1)  # it has to be defaulted to one since the first tab (0) is the frame that sends them back to the main menu.
        self.notebook.bind("<<NotebookTabChanged>>", self.main_menu_click)  # watches for tab changes to see if tab 0 was selected.

    def main_menu_click(self, event):  # begins main menu window creation.
        selected_tab = self.notebook.index(self.notebook.select())
        if selected_tab == 0:
            self.create_root()

    def create_root(self):  # creates main menu root.
        self.parent.destroy()
        main_menu_root = self.create_new_roots.create_root()
        MainMenu(main_menu_root, self.create_new_roots)
        main_menu_root.mainloop()


class ContentFrames:
    def __init__(self, notebook, parent, create_new_roots):
        self.notebook = notebook
        self.parent = parent
        self.create_new_roots = create_new_roots
        self.order_tree = None
        self.order = OrderInfo()
        self.customer = CustomerInfo()
        self.csvfile = CsvFileUsage()
        self.ordering_gui = OrderingGUI
        self.previous_bean = None
        self.bean_radio_buttons = []

        self.style = ttk.Style()  # changing radio button font appearance.
        self.style.configure("Custom.TRadiobutton", font=("Arial", 14))

    def frame_config(self, frame):  #This is a funcution that configures how my frames are setup,
        # this is used for each frame created to correctly position the banner at the bottom of the screen.

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

    def create_root(self): # sends you to main menu
        self.parent.destroy()
        main_menu_root = self.create_new_roots.create_root()
        MainMenu(main_menu_root, self.create_new_roots)
        main_menu_root.mainloop()

    def ordering_root_creation(self):  # sends you to ordering
        self.parent.destroy()
        ordering_gui_root = self.create_new_roots.create_root()
        OrderingGUI(ordering_gui_root, self.create_new_roots)
        ordering_gui_root.mainloop()

    def customer_details_tab(self):

        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")
        self.frame_config(frame)  #frame config

        pickup_or_delivery_label = tk.Label(frame, text="Pickup or Delivery?:", font=("Arial", 14))
        pickup_or_delivery_label.grid(row=0, column=0, sticky="SNW", columnspan=2, padx=5, pady=(100, 0))

        pickup_radio = ttk.Radiobutton(frame, text="Pickup", variable=self.order.pickup_or_delivery, value="Pickup",
                                       style="Custom.TRadiobutton", takefocus=0)
        pickup_radio.grid(row=0, column=1, sticky="SNW", columnspan=2, padx=(100, 0), pady=(100, 0))

        delivery_radio = ttk.Radiobutton(frame, text="Delivery", variable=self.order.pickup_or_delivery, value="Delivery",
                                         style="Custom.TRadiobutton", takefocus=0)
        delivery_radio.grid(row=0, column=1, sticky="SNW", padx=(200, 0), columnspan=2, pady=(100, 0))
        '''
        above is important for logic gates later, below the inputs are combobox for the possibility of autosuggest 
        in the future.
        '''
        name_label = tk.Label(frame, text="Name:", font=("Arial", 14))
        name_label.grid(row=1, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)

        name_combobox = ttk.Combobox(frame, textvariable=self.customer.name, width=30)
        name_combobox["values"] = ()
        name_combobox.grid(row=1, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        address_label = tk.Label(frame, text="Delivery Address:", font=("Arial", 14))
        address_label.grid(row=2, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)

        address_combobox = ttk.Combobox(frame, textvariable=self.customer.address, width=30)
        address_combobox["values"] = ()
        address_combobox.grid(row=2, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        phone_number_label = tk.Label(frame, text="Phone Number:", font=("Arial", 14))
        phone_number_label.grid(row=3, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)

        phone_number_combobox = ttk.Combobox(frame, textvariable=self.customer.phone_number, width=30)
        phone_number_combobox["values"] = ()
        phone_number_combobox.grid(row=3, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        email_label = tk.Label(frame, text="Email Address:", font=("Arial", 14))
        email_label.grid(row=4, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)

        email_combobox = ttk.Combobox(frame, textvariable=self.customer.email, width=30)
        email_combobox["values"] = ()
        email_combobox.grid(row=4, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        notes_label = tk.Label(frame, text="Notes:", font=("Arial", 14))
        notes_label.grid(row=5, column=0, sticky="NSW", columnspan=2, padx=5, pady=5)

        notes_combobox = ttk.Combobox(frame, textvariable=self.customer.notes, width=30)
        notes_combobox["values"] = ()
        notes_combobox.grid(row=5, column=1, columnspan=2, sticky="SNW", padx=(100, 5), pady=5)

        next_button = tk.Button(frame, text="Next", width=10, font=("Arial, 14"), command=lambda: self.notebook.select(2))
        next_button.grid(row=6, column=0, columnspan=2, sticky="SNW", pady=5)
        '''
        Banner navigation buttons, reused often
        '''
        back_button = tk.Button(frame, text="⌂", font="80", width=7, height=3, command=self.create_root)
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

    def bean_ordering_tab(self):

        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")
        self.frame_config(frame)  #frame config

        bean_label = tk.Label(frame, text="Bean type:", font=("Arial", 14))
        bean_label.grid(row=1, column=0, sticky="NW", columnspan=2, padx=5)
        '''
        I was having issues with on_bean_selected not updating correctly, luckly lambda allows it to run as the first 
        function that is processed by the button when created rather than the function. This meant that I could have 
        dynamically changing options for colour of roast.
        '''
        arabica_radio = ttk.Radiobutton(frame, text="Arabica", variable=self.order.bean, value="Arabica",
                                        command=lambda:self.on_bean_selected(frame), style="Custom.TRadiobutton", takefocus=0)
        arabica_radio.grid(row=1, column=1, sticky="NW", columnspan=2, padx=(50, 0))

        robusta_radio = ttk.Radiobutton(frame, text="Robusta", variable=self.order.bean, value="Robusta",
                                        command=lambda:self.on_bean_selected(frame), style="Custom.TRadiobutton", takefocus=0)
        robusta_radio.grid(row=1, column=1, sticky="NW", padx=(150, 0), columnspan=2)

        liberica_radio = ttk.Radiobutton(frame, text="Liberica", variable=self.order.bean, value="Liberica",
                                         command=lambda:self.on_bean_selected(frame), style="Custom.TRadiobutton", takefocus=0)
        liberica_radio.grid(row=1, column=1, sticky="NW", columnspan=2, padx=(250, 0))

        exclesa_radio = ttk.Radiobutton(frame, text="Excelsa", variable=self.order.bean, value="Excelsa",
                                        command=lambda:self.on_bean_selected(frame), style="Custom.TRadiobutton", takefocus=0)
        exclesa_radio.grid(row=1, column=1, sticky="NW", columnspan=2, padx=(350, 0))

        whole_or_ground_label = tk.Label(frame, text="Whole or Ground?:", font=("Arial", 14))
        whole_or_ground_label.grid(row=3, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)

        whole_radio = ttk.Radiobutton(frame, text="Whole", variable=self.order.whole_or_ground, value="Whole",
                                      style="Custom.TRadiobutton", takefocus=0)
        whole_radio.grid(row=3, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))

        ground_radio = ttk.Radiobutton(frame, text="Ground", variable=self.order.whole_or_ground, value="Ground",
                                       style="Custom.TRadiobutton", takefocus=0)
        ground_radio.grid(row=3, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))

        amount_label = tk.Label(frame, text="Amount:", font=("Arial", 14))
        amount_label.grid(row=4, column=0, sticky="NW", pady=(20, 0), columnspan=2, padx=5)

        amount_spinbox = ttk.Spinbox(frame, from_=0, to=5, textvariable=self.order.bean_amount, width=30)
        amount_spinbox.grid(row=4, column=1, sticky="NW", pady=(20, 0), padx=(25, 0))

        add_to_order_button = tk.Button(frame, text="+", font=("Arial", 14), command=self.add_to_order)
        add_to_order_button.grid(row=5, column=0, sticky="SWEN")

        add_to_order_label = tk.Label(frame, text="Add to Order", font=("Arial", 14))
        add_to_order_label.grid(row=5, column=1, sticky="SWN", padx=(5, 0))
        '''
        Banner navigation buttons, reused often
        '''
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

    def on_bean_selected(self, frame):  # this func is how I check what bean radio button has been selected
        selected_bean = self.order.bean.get()
        for button in self.bean_radio_buttons: # finds all radio buttons in the list, and deletes them from the UI
            button.grid_forget()
        self.bean_radio_buttons.clear()

        if selected_bean != self.previous_bean: # Check if the selected bean has changed
            self.bean_logic(selected_bean, frame)  # Call logic to update UI based on selected radio button
            self.previous_bean = selected_bean

    def bean_logic(self, selected_bean, frame):  # colour availability of each coffee bean type

            if selected_bean == "Robusta":
                bean_colour_label = tk.Label(frame, text="Bean colour:", font=("Arial", 14))
                bean_colour_label.grid(row=2, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
                light_radio = ttk.Radiobutton(frame, text="Light", variable=self.order.bean_colour, value="Light",
                                              style="Custom.TRadiobutton", takefocus=0)
                light_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(50, 0))
                self.bean_radio_buttons.append(light_radio)
                medium_radio = ttk.Radiobutton(frame, text="Medium", variable=self.order.bean_colour, value="Medium",
                                               style="Custom.TRadiobutton", takefocus=0)
                medium_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))
                self.bean_radio_buttons.append(medium_radio)
                dark_radio = ttk.Radiobutton(frame, text="Dark", variable=self.order.bean_colour, value="Dark",
                                             style="Custom.TRadiobutton", takefocus=0)
                dark_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))
                self.bean_radio_buttons.append(dark_radio)

            elif selected_bean == "Excelsa":
                bean_colour_label = tk.Label(frame, text="Bean colour:", font=("Arial", 14))
                bean_colour_label.grid(row=2, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
                light_radio = ttk.Radiobutton(frame, text="Light", variable=self.order.bean_colour, value="Light",
                                              style="Custom.TRadiobutton", takefocus=0)
                light_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(50, 0))
                self.bean_radio_buttons.append(light_radio)
                medium_radio = ttk.Radiobutton(frame, text="Medium", variable=self.order.bean_colour, value="Medium",
                                               style="Custom.TRadiobutton", takefocus=0)
                medium_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))
                self.bean_radio_buttons.append(medium_radio)

            else:
                bean_colour_label = tk.Label(frame, text="Bean colour:", font=("Arial", 14))
                bean_colour_label.grid(row=2, column=0, sticky="NW", columnspan=2, pady=(20, 0), padx=5)
                light_radio = ttk.Radiobutton(frame, text="Light", variable=self.order.bean_colour, value="Light",
                                              style="Custom.TRadiobutton", takefocus=0)
                light_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(50, 0))
                self.bean_radio_buttons.append(light_radio)
                medium_radio = ttk.Radiobutton(frame, text="Medium", variable=self.order.bean_colour, value="Medium",
                                               style="Custom.TRadiobutton", takefocus=0)
                medium_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(150, 0))
                self.bean_radio_buttons.append(medium_radio)
                dark_radio = ttk.Radiobutton(frame, text="Dark", variable=self.order.bean_colour, value="Dark",
                                             style="Custom.TRadiobutton", takefocus=0)
                dark_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(250, 0))
                self.bean_radio_buttons.append(dark_radio)
                extra_dark_radio = ttk.Radiobutton(frame, text="Extra Dark", variable=self.order.bean_colour, value="Extra Dark",
                                                   style="Custom.TRadiobutton", takefocus=0)
                extra_dark_radio.grid(row=2, column=1, sticky="NW", columnspan=2, pady=(20, 0), padx=(350, 0))
                self.bean_radio_buttons.append(extra_dark_radio)

    def add_to_order(self): # forms order information seen on the next tab
        bean_prices = {"Arabica": 38.50, "Robusta": 38.50, "Liberica": 33.50, "Excelsa": 33.50}  # -placeholders for
        # when I add csv func to the bean types

        selected_bean_type = self.order.bean.get()
        self.bean_price = bean_prices.get(selected_bean_type)
        self.order.calculated_cost = (self.bean_price) * self.order.bean_amount.get() + (
            5 if self.order.pickup_or_delivery.get() == "Delivery" else 0) #calcs price

        order_info = {  # creates order list
            "date": f"{datetime.now().strftime('%Y-%m-%d')}",
            "ID": self.csvfile.get_next_id(),
            "order": f"{self.order.bean.get()} ({self.order.bean_colour.get()}), {self.order.whole_or_ground.get()}, {self.order.bean_amount.get()} Kg",
            "cost": f"${self.order.calculated_cost:.2f}",
            "delivery": self.order.pickup_or_delivery.get(),
            "address": self.customer.address.get(),
            "notes": self.customer.notes.get()
        }
        self.update_treeview(order_info)  # updates treeview to show order information
        self.notebook.select(3) # changes to next tab

    def update_treeview(self, order_info):  # updates over information

        self.order_tree.delete(*self.order_tree.get_children())
        self.order_tree.insert("", "end", values=(
        order_info["order"], order_info["cost"]))

    def confirm_order_tab(self):

        frame = ttk.Frame(self.notebook, borderwidth=0, relief="flat")
        self.frame_config(frame)  # frame config

        style = ttk.Style() # #styles treeview
        style.configure("Treeview.Heading", background="#e0e0e0", foreground="black", font=("Arial", 14),
                        padding=[0, 5])
        style.configure("Treeview", rowheight=25)

        order_label = tk.Label(frame, text="Order Summary:", font=("Arial", 14))
        order_label.grid(row=1, column=0, sticky="NW", columnspan=2)

        self.order_tree = ttk.Treeview(frame, columns=("order", "cost"), show="headings", height=1)
        self.order_tree.heading("order", text="Order")
        self.order_tree.heading("cost", text="Cost")
        self.order_tree.column("order", width=300, anchor="center")
        self.order_tree.column("cost", width=75, anchor="center")
        self.order_tree.grid(row=2, column=0, sticky="SWEN", columnspan=5)

        cancel_button = tk.Button(frame, text="Cancel Order", font=("Arial", 14), height=2, command=self.create_root)
        cancel_button.grid(row=7, column=0, columnspan=2, sticky="SW", pady=(0, 10))

        confirm_button = tk.Button(frame, text="Confirm Order", font=("Arial", 14), height=2,
                                   command=lambda:self.write_information()) # needed lambda here so that write
        # informtion isn't called when the information still doesn't exist since these windows are
        # created when the window is created.
        confirm_button.grid(row=7, column=3, columnspan=2, sticky="SE", pady=(0, 10))
        '''
        Banner navigation buttons, reused often
        '''
        back_button = tk.Button(frame, text="←", font="80", width=7, height=3, command=lambda: self.notebook.select(2))
        back_button.grid(row=8, column=0, sticky="SW")
        next_button = tk.Button(frame, text="⌂", font="80", width=7, height=3, command=self.create_root)
        next_button.grid(row=8, column=4, sticky="SW")
        current_tab = tk.Label(frame, text="Kahawa Coffee™ - Confirm Order", font=("Arial", 14), fg="white", bg="black")
        current_tab.grid(row=8, column=1, sticky="SWEN", pady=10, columnspan=3)
        banner = tk.Label(frame, bg="black", width=200, height=4)
        banner.grid(row=8, column=0, columnspan=5, sticky="SWEN")
        banner.lower()

        return frame

    '''
    Error prevention and writing information to csv files all in one...... This could be optimised but I have no time.
    '''

    def write_information(self):
        bean_prices = {"Arabica": 38.50, "Robusta": 38.50, "Liberica": 33.50, "Excelsa": 33.50}  # -placeholders for
        # when I add csv func to the bean types
        error_messages = [""]  # creates list where error messages will be logged
        required_order_fields = ["date", "ID", "order", "cost", "delivery", "address"]  # different possible errors
        required_customer_fields = ["ID", "name", "phone number", "email"]  # different possible errors

        selected_bean_type = self.order.bean.get()
        self.bean_price = bean_prices.get(selected_bean_type)
        bean_amount = self.order.bean_amount.get()
        '''
        missing bean order information checks
        '''
        if self.order.bean.get() == "":
            error_messages.append(f"Missing required order information: Bean type")
        if self.order.bean_colour.get() == "":
            error_messages.append(f"Missing required order information: Bean colour")
        if self.order.whole_or_ground.get() == "":
            error_messages.append(f"Missing required order information: Bean Whole or Ground")

        if bean_amount > 5 or bean_amount <= 0:
            error_messages.append("Bean amount must be greater than 0kg and under 5kg.")
        else:
            try:
                self.order.calculated_cost = (self.bean_price * bean_amount) + (
                    5 if self.order.pickup_or_delivery.get() == "Delivery" else 0)
            except:
                error_messages.append(f"Missing required order information: {bean_prices.keys()}")


        self.order_info = {
            "date": f"{datetime.now().strftime('%Y-%m-%d')}",
            "ID": self.csvfile.get_next_id(),
            "order": f"{self.order.bean.get()} ({self.order.bean_colour.get()}), {self.order.whole_or_ground.get()}, {self.order.bean_amount.get()} Kg",
            "cost": f"${self.order.calculated_cost:.2f}",
            "delivery": self.order.pickup_or_delivery.get(),
            "address": self.customer.address.get(),
            "notes": self.customer.notes.get()
        }


        self.customer_info = {
            "ID": self.csvfile.get_next_id(),
            "name": self.customer.name.get(),
            "phone number": self.customer.phone_number.get(),
            "email": self.customer.email.get(),
            "address": self.customer.address.get(),
            "notes": self.customer.notes.get()
        }
        '''
        more error prevention checks.....
        '''
        for i in required_order_fields:
            if i == "address" and self.order_info["delivery"] == "Pickup":
                continue
            if not self.order_info.get(i):
                error_messages.append(f"Missing required order information: {i}")

        for i in required_customer_fields:
            if i == "phone number":
                if not str(self.customer_info[i]).isdigit():
                    error_messages.append("\n Invalid Phone number")
            if i == "email":
                if "@" not in self.customer_info[i]:
                    error_messages.append("\n Invalid Email")
            if not self.customer_info.get(i):
                error_messages.append(f"\nMissing required customer information: {i}")

        if error_messages != [""]:  # If there are any error messages, display them in a message box
            self.show_error_popup(error_messages)
        else:
            self.csvfile.write_customer_data(self.customer_info)  # write to csv files
            self.csvfile.write_order_data(self.order_info)
            self.create_root_orders_view()

    def show_error_popup(errors, error_messages): # displays errors in a message pop up
        error_window = tk.Toplevel()
        error_window.title("Errors with order")
        msg = tk.Message(error_window, text=error_messages, width=300)
        msg.pack(padx=20, pady=20)
        close_button = tk.Button(error_window, text="Close", command=error_window.destroy)
        close_button.pack(pady=(0, 20))
    def create_root_orders_view(self):
        self.parent.destroy()
        view_order_gui_root = self.create_new_roots.create_root()
        ViewOrders(view_order_gui_root, create_new_roots)
        view_order_gui_root.mainloop()


@dataclass # used to handle variables input easier, no more .self clutter in the __init__
class CustomerInfo:
    name: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    address: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    phone_number: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    email: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    notes: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))


@dataclass # used to handle variables input easier, no more .self clutter in the __init__
class OrderInfo:
    pickup_or_delivery: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    bean: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    whole_or_ground: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    bean_colour: tk.StringVar = field(default_factory=lambda: tk.StringVar(value=""))
    bean_amount: tk.IntVar = field(default_factory=tk.IntVar)
    calculated_cost: float = 0.0


class CreateNewRoots:  # used when needing to make a new window
    def create_root(self):
        root = tk.Tk()
        root.geometry("950x660+300+300")
        root.configure(bg="white")
        root.title("Kahawa Coffee™")
        root.resizable(False, False)
        return root


if __name__ == "__main__":  # the most important piece of code, hasn't been touched since day 1 since it was that good.
    root = tk.Tk()
    root.geometry("950x660+300+300")
    root.configure(bg="white")
    root.title("Kahawa Coffee™")
    root.resizable(False, False)
    create_new_roots = CreateNewRoots()
    app = MainMenu(root, create_new_roots)
    root.mainloop()

'''
This was okay, frames are terrible to work with when they refuse to do things without pulling errors at the same time
'''
