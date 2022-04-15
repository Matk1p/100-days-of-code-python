from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)  # the window is going to scale according to the amount of items, buttons etc

# Creating Label, using the Tkinter.label class
my_label = Label(text="First label", font=("Arial", 24, "bold"))
# my_label.pack()  # this is needed to show the label in the window
# my_label.place(x=100, y=100)  # can use place to specify the coordinate of each widget
my_label.grid(column=0, row=0)  # imagines there is a grid behind
# packer is essentially the methods needed to arrange the location of the items

# the different ways to configure the components created
my_label["text"] = "New text"
my_label.config(text="My title")


# need functions to get the button to carry out a task
def button_clicked(*args):
    new_text = input.get()
    my_label.config(text=new_text)


# creating button object
button = Button(text="Click me",
                command=button_clicked)  # this will essentially call the function when button is clicked
button.grid(column=1, row=1)

# creating a new button
new_button = Button(text="new button")
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()  # this line will keep the GUI window open
