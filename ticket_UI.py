from tkinter import *
from tkinter import messagebox


def calculate_cost():
    distance = int(distance_entry.get())
    departure_date = int(departure_date_entry.get())
    service_class = service_class_var.get()

    if distance < 500:
        cost = 100
    elif 500 <= distance <= 1000:
        if departure_date <= 7:
            cost = distance * 0.10
        elif departure_date <= 30:
            cost = distance * 0.08
        elif departure_date <= 90:
            cost = distance * 0.06
    else:
        if departure_date <= 7:
            cost = distance * 0.30
        elif departure_date <= 30:
            cost = distance * 0.25
        elif departure_date <= 90:
            cost = distance * 0.20

    if service_class == "Business":
        cost *= 2
    elif service_class == "First":
        cost *= 3

    messagebox.showinfo("Cost Calculation", f"The cost is: ${cost:.2f}")


# Create the UI
root = Tk()
root.title("Flight Cost Calculator")

# Distance
distance_label = Label(root, text="Distance (in miles):")
distance_label.pack()
distance_entry = Entry(root)
distance_entry.pack()

# Departure Date
departure_date_label = Label(root, text="Departure Date (in days):")
departure_date_label.pack()
departure_date_entry = Entry(root)
departure_date_entry.pack()

# Service Class
service_class_label = Label(root, text="Service Class:")
service_class_label.pack()

service_class_var = StringVar()
service_class_var.set("Economy")

service_class_radio_economy = Radiobutton(root, text="Economy", variable=service_class_var, value="Economy")
service_class_radio_economy.pack()

service_class_radio_business = Radiobutton(root, text="Business", variable=service_class_var, value="Business")
service_class_radio_business.pack()

service_class_radio_first = Radiobutton(root, text="First", variable=service_class_var, value="First")
service_class_radio_first.pack()

# Calculate Button
calculate_button = Button(root, text="Calculate", command=calculate_cost)
calculate_button.pack()

root.mainloop()

