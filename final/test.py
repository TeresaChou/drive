import tkinter as tk
import tkinter.ttk as ttk
import random
import time

# build the window
window = tk.Tk()
window.title("Vision Checker")
window.geometry("1000x800")
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)

# label candidates
pic = ["Up", "Down", "Right", "Left"]
picpos = random.randint(0,3)

# function for changing candidate
def change(dire):
    global picpos
    if picpos == dire:
        result.config(text="Correct!", fg="green")
    else: 
        result.config(text="Wrong!", fg="red")
    window.update_idletasks()
    time.sleep(2)
    result.config(text="")
    picpos = random.randint(0,3)
    label.config(image=gifIm[picpos])
    label.image = gifIm[picpos]
    # picvar.set(pic[picpos])

# load the pictures
gifUp = tk.PhotoImage(file="image/Up.gif")
gifDown = tk.PhotoImage(file="image/Down.gif")
gifLeft = tk.PhotoImage(file="image/Left.gif")
gifRight = tk.PhotoImage(file="image/Right.gif")
gifIm = [gifUp, gifDown, gifLeft, gifRight]
scale_w = 2
scale_h = 2
gifUp.subsample(scale_w, scale_h)
gifDown.subsample(scale_w, scale_h)
gifLeft.subsample(scale_w, scale_h)
gifRight.subsample(scale_w, scale_h)

# add the picture
label = tk.Label(window, image=gifIm[picpos])
label.grid(column=2, row=2, columnspan=3, rowspan=2, sticky="NEWS")

# add text labels
picvar = tk.StringVar()
picvar.set(pic[picpos])
#label = tk.Label(
#        window, 
#        textvariable=picvar, 
#        font=("Arial", 50)
#        )
result = tk.Label(
        window, 
        text="",
        font=("Arial", 20),
        width=10, height=1
        )
result.grid(column=3, row=4)

# add buttons
buttonUp = ttk.Button(window, text="Up", command=lambda:change(0))
buttonUp.grid(column=3, row=1)
buttonDown = ttk.Button(window, text="Down", command=lambda:change(1))
buttonDown.grid(column=3, row=5)
buttonLeft = ttk.Button(window, text="Left", command=lambda:change(2))
buttonLeft.grid(column=1, row=3)
buttonRight = ttk.Button(window, text="Right", command=lambda:change(3))
buttonRight.grid(column=5, row=3)


# bind the keyboard
window.bind("<Up>", lambda event: change(0))
window.bind("<Down>", lambda event: change(1))
window.bind("<Left>", lambda event: change(2))
window.bind("<Right>", lambda event: change(3))

window.mainloop()
