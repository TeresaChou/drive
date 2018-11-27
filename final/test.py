import tkinter as tk
import ttk

# build the window
root = tk.Tk()
root.title("Vision Checker")

# add a text label
label = tk.Label(root, text="Picture")
label.grid(column=2, row=2)

# add buttons
buttonUp = tk.Button(root, text="Up")
buttonUp.grid(column=2, row=1)
buttonDown = tk.Button(root, text="Down")
buttonDown.grid(column=2, row=3)
buttonRight = tk.Button(root, text="Right")
buttonRight.grid(column=3, row=2)
buttonLeft = tk.Button(root, text="Left")
buttonLeft.grid(column=1, row=2)

root.mainloop()
