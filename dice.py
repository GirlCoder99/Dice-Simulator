import tkinter
import random
root = tkinter.Tk() #Accessing TK
root.geometry("700x450") #Creating Interface of Size 700 * 450
root.title("Roll Dice")

label = tkinter.Label(root, font=("times", 200)) #increases the size of the GUI Elements

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text = f'{random.choice(dice)} {random.choice(dice)}')
    label.pack() #It is a gemoetry manager organizes the widgets in blocks before placing them in the parent widget

button = tkinter.Button(root, text = "Time to roll...", command = roll)
button.pack()

button.place(x = 330, y = 0)

root.mainloop()