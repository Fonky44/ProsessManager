import tkinter as tk
import Main

root = tk.Tk()

Frame = tk.Frame(root, width=500, height=500)
Name = tk.Label(root, text = "Name")

Frame.grid_propagate(0)
Frame.grid()
Name.grid()

root.mainloop()