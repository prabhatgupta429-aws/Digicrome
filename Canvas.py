import tkinter as tk
import math

# Create the main window
root = tk.Tk()

# Set the window size
root.geometry("900x600")

# Create the canvas
canvas = tk.Canvas(root, width=900, height=600)
canvas.pack()

# Draw the green rectangle for the top part of the flag
canvas.create_rectangle(0, 0, 900, 200, fill="#FF9933", outline="")

# Draw the white rectangle for the middle part of the flag
canvas.create_rectangle(0, 200, 900, 400, fill="white", outline="")

# Draw the green rectangle for the bottom part of the flag
canvas.create_rectangle(0, 400, 900, 600, fill="#138808", outline="")

# Draw the navy blue wheel in the center
canvas.create_oval(250, 100, 650, 500, fill="#000080", outline="")

# Draw the 24 spokes of the wheel
for i in range(24):
    x0 = 450
    y0 = 300
    x1 = x0 + 200 * math.cos(math.radians(i * 15))
    y1 = y0 - 200 * math.sin(math.radians(i * 15))
    canvas.create_line(x0, y0, x1, y1, fill="white", width=8)

# Run the tkinter main loop
root.mainloop()