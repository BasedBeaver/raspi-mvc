import tkinter as tk
import controller as c


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        main_canvas = tk.Canvas(parent, bg="dark green")
        main_canvas.pack(fill=tk.BOTH, expand=True)

        # <create the rest of your GUI here>


if __name__ == "__main__":
    root = tk.Tk()
    # root.geometry("800x600")
    MainApplication(root).pack(fill=tk.BOTH, expand=False)
    root.mainloop()
