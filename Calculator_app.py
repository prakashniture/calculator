from tkinter import *

# toolkit interface
claculator_root = Tk()

# width x height
claculator_root.geometry("500x500")

# width, height
claculator_root.minsize(400,400)
claculator_root.maxsize(1200,988)


calc = Label(text="This is my first calculator")
calc.pack()


claculator_root.mainloop()