import tkinter as tk
from tkinter import ttk
from manage_api import search_by_cod
from p_touch_commands import send_to_printer

# Get item number from GUI input field, search API for item name
def print_item_no(*args):
   item_no = item_no_var.get()
   item_name = search_by_cod(item_no)
   # Send info to P-Touch editor and print
   send_to_printer(item_no, item_name)

# Exit function
def on_exit():
   root.destroy()

# Create the main window of GUI
root = tk.Tk()
root.title("Print product label")

# Set a custom style for themed widgets
style = ttk.Style()
style.configure('TButton', padding=10, font=('Helvetica', 12))

# Create and place the widgets on GUI
item_no_label = ttk.Label(root, font=('Helvetica', 12), padding=10, text="Item no.")
item_no_label.grid(row=0, column=0, padx=10, pady=10)

item_no_var = tk.StringVar()
item_no_entry = ttk.Entry(root, textvariable=item_no_var, width=20, font=('Helvetica', 12))
item_no_entry.grid(row=0, column=1, padx=10, pady=10)

print_button = ttk.Button(root, text="Print", command=print_item_no)
print_button.grid(row=1, column=0, columnspan=2, pady=10)

exit_button = ttk.Button(root, text="Exit", command=on_exit)
exit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Bind the Enter key to the print_item_no function
root.bind('<Return>', print_item_no)

# Run the application
root.mainloop()