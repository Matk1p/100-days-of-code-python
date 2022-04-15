from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def convert():
    result.config(text="{:.2f}".format(int(mile_input.get()) * 1.60934))


# Entry
mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

# Miles label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# text label
text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

# result label
result = Label(text="0")
result.grid(column=1, row=1)

# km label
km = Label(text="Km")
km.grid(column=2, row=1)

# Button
calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
