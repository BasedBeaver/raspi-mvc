import tkinter as tk


class Model:

    def desk_lamp(self):
        print("Add ethernet package")

class view(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        main_canvas = tk.Canvas(parent, bg="dark green")
        main_canvas.pack(fill=tk.BOTH, expand=True)

        desk_lamp_button = tk.Button(main_canvas, text="Desk Lamp ON/OFF", command=self.desk_lamp)
        desk_lamp_button.pack(side="right")

    def desk_lamp(self):
        print("YAY")
        c.desk_lamp()

        # <create the rest of your GUI here>


class Controller:
    def __init__(self):
        self.model = Model()
        self.root = tk.Tk()
        self.root.geometry("300x200")
        view(self.root).pack(fill=tk.BOTH, expand=False)

    def run(self):
        self.root.title("RaspberryPi Smarthome Controller")
        self.root.deiconify()
        self.root.mainloop()

    def desk_lamp(self):
        print("c.yay")
        self.model.desk_lamp()


if __name__ == "__main__":
    c = Controller()
    c.run()
