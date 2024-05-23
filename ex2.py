from tkinter import *
from tkinter import Toplevel, scrolledtext, END
from experta import *

# Define GUI functions
def calculate_bill(facts):
    total = sum(qty * price for qty, price in facts.values())
    return total

def show_bill(facts):
    for item, (_, price) in facts.items():
        entry_value = entries[items.index(item)].get()
        quantity = int(entry_value) if entry_value else 0
        facts[item][0] = quantity

    total_bill = calculate_bill(facts)
    display_bill(total_bill, facts)

def display_bill(total_bill, facts):
    global bill_window, bill_text
    bill_window = Toplevel(window)
    bill_window.geometry("500x300")
    bill_window.title("Your Bill")

    bill_text = scrolledtext.ScrolledText(bill_window, width=50, height=10, font=("Helvetica", 12))
    bill_text.pack(pady=10)

    bill_text.insert(END, "Selected Items:\n")
    for item, (qty, price) in facts.items():  
        if qty > 0:
            bill_text.insert(END, f"{item}: {qty}\n")
    bill_text.insert(END, f"\nTotal Price: ${total_bill}")

    edit_button = Button(bill_window, text="Edit", command=lambda: edit_quantity(bill_text, facts), bg="gray", fg="white", font=("Arial", 14, "bold"))
    edit_button.pack(side=LEFT, padx=10, pady=10)
    
    def confirm_billing():
        engine.declare(Fact(action='confirm_billing'))
        engine.run()
    confirm_button = Button(bill_window, text="Confirm", command=confirm_billing, bg="green", fg="white", font=("Arial", 14, "bold"))
    confirm_button.pack(side=LEFT, padx=10, pady=10)

    def cancel_billing():
        engine.declare(Fact(action='cancel_billing'))
        engine.run()
    cancel_button = Button(bill_window, text="Cancel", command=cancel_billing, bg="red", fg="white", font=("Arial", 14, "bold"))
    cancel_button.pack(side=LEFT, padx=10, pady=10)

def edit_quantity(bill_text, facts):
    edit_window = Toplevel(window)
    edit_window.title("Edit Quantity")

    labels = []
    entry_widgets = []
    for idx, (item, _) in enumerate(facts.items()):
        label = Label(edit_window, text=item, font=("Arial", 14))
        label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
        labels.append(label)

        entry = Entry(edit_window, font=("Arial", 14))
        entry.grid(row=idx, column=1, padx=10, pady=5, sticky="e")
        entry.insert(0, str(facts[item][0]))  
        entry_widgets.append(entry)

    def save_edits():
        for idx, (item, _) in enumerate(facts.items()):
            quantity = int(entry_widgets[idx].get()) if entry_widgets[idx].get() else 0
            facts[item][0] = quantity
        edit_window.destroy()
        bill_text.delete(1.0, END)
        bill_text.insert(END, "Selected Items:\n")
        for item, (qty, price) in facts.items():
            if qty > 0:
                bill_text.insert(END, f"{item}: {qty}\n")
        total = calculate_bill(facts)
        bill_text.insert(END, f"\nTotal Price: ${total}")
        engine.declare(Fact(action='edit_bill'))
        engine.run()

    save_button = Button(edit_window, text="Save", command=save_edits, bg="blue", fg="white", font=("Arial", 14, "bold"))
    save_button.grid(row=len(facts), column=0, columnspan=2, padx=10, pady=10)

# Experta System Code
class find_bill(KnowledgeEngine):
    def __init__(self, window):
        super().__init__()
        self.window = window

    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_bill")

    @Rule(Fact(action='confirm_billing'))
    def confirm_billing(self):
        confirmation_window = Toplevel(self.window)
        confirmation_label = Label(confirmation_window, text="Billing confirmed successfully.", font=("Arial", 14))
        confirmation_label.pack(padx=10, pady=10)
        bill_window.destroy()

    @Rule(Fact(action='cancel_billing'))
    def cancel_billing(self):
        cancelation_window = Toplevel(self.window)
        cancelation_label = Label(cancelation_window, text="Bill Canceled.", font=("Arial", 14))
        cancelation_label.pack(padx=10, pady=10)
        bill_window.destroy()

    @Rule(Fact(action='edit_bill'))
    def edit_bill(self):
        print("The bill has been edited.")

def main():
    global window, items, entries, facts, engine

    response = input("Would you like to display the GUI? (yes/no): ").strip().lower()
    if response == "no":
        print("Exiting the application.")
        return
    elif response != "yes":
        print("Invalid input. Exiting the application.")
        return

    window = Tk()
    window.geometry("900x500")
    original_image = PhotoImage(file='sushi.png')
    background_label = Label(window, image=original_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    label8 = Label(window, text="SusHiyaki Restaurant", font=("Arial", 28, "bold"), fg="white", background="black")
    label8.place(x=800, y=20, anchor="center")
    label1 = Label(window, text="Menu", font=("Arial", 28, "bold"), fg="white", background="black")
    label1.place(x=1200, y=70)

    menu_items = ['Aloo Paratha Rs 30', 'Samosa Rs 5', 'Pizza Rs 150', 'Chilli Potato Rs 50', 'Chowmein Rs 70', 'Gulab Jamun Rs 35']
    for i, item in enumerate(menu_items):
        label = Label(window, text=item, font=("Arial", 14), fg="white", background="black")
        label.place(x=1200, y=200 + i * 40)

    items = ['Aloo Paratha', 'Samosa', 'Pizza', 'Chilli Potato', 'Chowmein', 'Gulab Jamun']
    entries = []
    for i, item in enumerate(items):
        label = Label(window, text=item, font=("Arial", 14), fg="white", background="black")
        label.place(x=30 if i < 3 else 400, y=200 + (i % 3) * 40)
        entry = Entry(window, font=("Arial", 14))
        entry.place(x=150 if i < 3 else 700, y=200 + (i % 3) * 40)
        entries.append(entry)

    facts = {'Aloo Paratha': [0, 30],
             'Samosa': [0, 5],
             'Pizza': [0, 150],
             'Chilli Potato': [0, 50],
             'Chowmein': [0, 70],
             'Gulab Jamun': [0, 35]}

    check_button = Button(window, text="Check Bill", font=("Arial", 18), command=lambda: show_bill(facts), bg="black", fg="white")
    check_button.place(x=700, y=600)
    
   # engine for the execution.
    engine = find_bill(window)
    while True:
        engine.reset()  
        engine.run()  
        print("Would you like to make another order?")
        if input().strip() == "no":  
            break
            window.mainloop()

if __name__ == "__main__":
    main()
