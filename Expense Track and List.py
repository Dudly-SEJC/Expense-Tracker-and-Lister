# Reference https://flexiple.com/python/python-classes-objects
# https://stackoverflow.com/questions/22698980/python-tkinter-why-is-it-root-mainloop-and-not-app-mainloop
# To use this program Enter your Expense in $ format, it is not specified, but you may add any necessary symbol --
# -- whether that be decimals or dollar sign, Example: $500.00 or 500.00 or 500 can be inputted
# Same goes for the description, anything may be added
# Expense will be displayed on the LEFT of the GUI list and Description to the RIGHT list.

#Importing tkinter to run GUIs
import tkinter as tk
# Setting class blueprint for certain functions
class ExpenseTracker: #Use of class, __init__, and self, referenced from flexiple.com,(#lines 9-51)
    def __init__(self, root):
        self.root = root #allows method of root
        self.root.title("Expense Tracker") #TITLE of GUI window
        self.root.geometry("330x350") #size of main GUI window
        self.root.configure(background="cornflowerblue") #color of main GUI window

        # Expense widget LABEL & ENTRY prompt
        self.expense_label = tk.Label(root, text="Enter Expense:", font="MongolianBaiti", background="cornflowerblue") #Label
        self.expense_label.pack() #positioning of label
        self.expense_entry = tk.Entry(root, background="lightgreen") #ENTRY, with background color
        self.expense_entry.pack() #positioning of entry

        # Description of expense widget LABEL & ENTRY prompt
        self.description_label = tk.Label(root, text="Description:", font="MongolianBaiti", background="cornflowerblue") #Label
        self.description_label.pack() #positioning of label
        self.description_entry = tk.Entry(root, background="lightgreen") #ENTRY, with background color
        self.description_entry.pack() #positioning of entry

        # Add Transaction BUTTON widget
        self.add_button = tk.Button(root, text="Add Transaction", width=13, command=self.add_expense) #BUTTON - connected to Def
        self.add_button.pack(pady=6) #pady adjusts vertical positioning

        # Sets Expense listbox, where output will be displayed
        self.expense_listbox = tk.Listbox(root, width=15, background="lightsteelblue") #LIST
        self.expense_listbox.pack(side=tk.LEFT, padx=5,pady=5) #side=tk.left sets to left of GUI root window

        # Sets Description listbox, where output will be displayed
        self.description_listbox = tk.Listbox(root, width=35, background="lightsteelblue") #LIST
        self.description_listbox.pack(side=tk.LEFT,padx=5,pady=5) #by default another side=tk.left is stacked

#Making sure that entry into prompts is added into the list, when Add Expense button is clicked
    # Creates a condition and a path for where the ENTRY of Expense and Description will go
    def add_expense(self):
        expense = self.expense_entry.get() #sets variable for condition
        description = self.description_entry.get() #sets variable for condition
        if expense:
            self.expense_listbox.insert(tk.END, expense) #inserts expense to listbox
            self.expense_entry.delete(0, tk.END) #clears the entry for expense prompt once button is pressed
        if description:
            self.description_listbox.insert(tk.END, description) #inserts description to listbox
            self.description_entry.delete(0, tk.END) #clears the entry for description prompt once button is pressed

if __name__ == "__main__": #condition to check script for direct run
    root = tk.Tk() #root GUI window
    app = ExpenseTracker(root) #sets the class or the program Expense Tracker to be looped
    root.mainloop() #allows for program to run

# I have written lines 9-51 myself, with use of reference from flexiple.com (link is at the top).
# However, lines 53-56 were referenced from a stackoverflow.com forum (link is at the top).