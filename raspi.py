import tkinter as tk
import os


class Model:

    def desk_lamp(self):
        print("Turn On/Off desk lamp")

    def magic_package(self):
        print("Turn On computer")
        os.system('sudo /home/CitizenSwagger/wol.sh')


class View(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.main_canvas = tk.Canvas(parent, bg="dark green")
        self.main_canvas.pack(fill=tk.BOTH, expand=True)

        self.desk_lamp_button = tk.Button(self.main_canvas, text="Desk Lamp ON/OFF", command=self.desk_lamp)
        self.desk_lamp_button.pack(side="right", expand=True, fill=tk.BOTH)

        self.computer_button = tk.Button(self.main_canvas, text="Turn On Computer", command=self.magic_package)
        self.computer_button.pack(side="left", expand=True, fill=tk.BOTH)

    def desk_lamp(self):
        c.desk_lamp()

    def magic_package(self):
        c.magic_package()

        # <create the rest of your GUI here>


class Controller:
    def __init__(self):
        self.model = Model()
        self.root = tk.Tk()
        self.root.geometry("300x200")
        View(self.root).pack(fill=tk.BOTH, expand=False)

    def run(self):
        self.root.title("RaspberryPi Smarthome Controller")
        self.root.deiconify()
        self.root.mainloop()

    def desk_lamp(self):
        self.model.desk_lamp()

    def magic_package(self):
        self.model.magic_package()


if __name__ == "__main__":
    c = Controller()
    c.run()
