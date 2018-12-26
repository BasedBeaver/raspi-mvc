import tkinter as tk
import os
import datetime as dt


class Model:

    def desk_lamp(self):
        #TODO: get hardware from ikea
        return False

    def magic_package(self):
        os.system('sudo /home/CitizenSwagger/wol.sh')


class View(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.main_canvas = tk.Canvas(parent, bg="black", borderwidth=0)
        self.main_canvas.pack(fill=tk.BOTH, expand=True)

        self.button_canvas = tk.Canvas(self.main_canvas, bg="black", borderwidth=0)
        self.button_canvas.pack(side="left", fill=tk.BOTH, expand=True)

        self.info_canvas = tk.Canvas(self.main_canvas, bg="black", borderwidth=0)
        self.info_canvas.pack(side="right", fill=tk.BOTH, expand=True)

        self.desk_lamp_button = tk.Button(self.button_canvas, text="Desk Lamp ON/OFF", bg="black", fg="white",
                                          activebackground="black", activeforeground="white",
                                          borderwidth=0, command=self.desk_lamp)
        self.desk_lamp_button.pack(side="top", expand=True, fill=tk.BOTH)

        self.computer_button = tk.Button(self.button_canvas, text="Turn On Computer", bg="black", fg="white",
                                         activebackground="black", activeforeground="white",
                                         borderwidth=0, command=self.magic_package)
        self.computer_button.pack(side="bottom", expand=True, fill=tk.BOTH)

        self.info_textfield = tk.Text(self.info_canvas, bg="black", fg="white", font=("Helvetica", 16))
        self.info_textfield.configure(state=tk.DISABLED, borderwidth=0)
        self.info_textfield.pack(fill=tk.BOTH, expand=True)

    def desk_lamp(self):
        time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        string = '---' + str(time) + ': ' + 'Turn On/Off desk lamp---'
        self.info_textfield.config(state=tk.NORMAL)
        self.info_textfield.insert(tk.END, string)
        # self.info_textfield.tag_configure("center", justify='center')
        # self.info_textfield.tag_add("center", 1.0, "end")
        self.info_textfield.insert(tk.END, '\n')
        self.info_textfield.see(tk.END)
        self.info_textfield.config(state=tk.DISABLED)

        c.desk_lamp()

    def magic_package(self):
        time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        string = '---' + str(time) + ': ' + 'Turn On computer---'
        self.info_textfield.config(state=tk.NORMAL)
        self.info_textfield.insert(tk.END, string)
        # self.info_textfield.tag_configure("center", justify='center')
        # self.info_textfield.tag_add("center", 1.0, "end")
        self.info_textfield.insert(tk.END, '\n')
        self.info_textfield.see(tk.END)
        self.info_textfield.config(state=tk.DISABLED)
        c.magic_package()


class Controller:
    def __init__(self):
        self.model = Model()
        self.root = tk.Tk()
        self.root.geometry("300x200")
        View(self.root).pack(fill=tk.BOTH, expand=False)

    def run(self):
        self.root.title("RaspberryPi SmartHome Controller")
        self.root.deiconify()
        self.root.mainloop()

    def desk_lamp(self):
        self.model.desk_lamp()

    def magic_package(self):
        self.model.magic_package()


if __name__ == "__main__":
    c = Controller()
    c.run()
