import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("RaspberryPi Smarthome Controller")

background_canvas = tk.Canvas(root, bg="dark green")
background_canvas.pack(fill=tk.BOTH, expand=True)

root.mainloop()