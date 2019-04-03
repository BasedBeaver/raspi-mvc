"""
On raspi:
export DISPLAY=:0
before starting
"""

import tkinter as tk
import os
import datetime as dt
import threading
import collections
# import speech_recognition as sr


class VoiceThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            with sr.Microphone() as source:  # set speech source to Microphone
                print("Speak Anything :")
                audio = recorder.listen(source)  # listen to the source
                try:
                    text = recorder.recognize_google(audio)  # use recognizer to convert our audio into text part
                    if text == "Jarvis turn on computer":
                        os.system('sudo /home/CitizenSwagger/wol.sh')
                except:
                    continue


class PhoneThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            e = threading.Event()
            e.wait(timeout=10)
            ret = os.system("timeout 0.5 ping -c 1 192.168.0.102")
            if ret != 0:
                print("Offline")
            else:
                print("Online")


class Model:

    info_list = collections.deque()

    def get_info_list(self, choice):
        info = ''
        time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if choice == 'lamp':
            info = '---' + str(time) + ': ' + 'Turn On/Off desk lamp---'
        elif choice == 'magic':
            info = '---' + str(time) + ': ' + 'Turn On computer---'

        if len(self.info_list) < 25:
            self.info_list.append(info)
        else:
            self.info_list[0] = info
            self.info_list.rotate(-1)

        return self.info_list

    def desk_lamp(self):
        # TODO: get API for hardware
        return False

    def magic_package(self):
        # os.system('sudo /home/CitizenSwagger/wol.sh')
        return False;


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
        info_list = c.get_info_list('lamp')
        self.info_textfield.config(state=tk.NORMAL)
        self.info_textfield.delete(1.0, tk.END)
        for info in info_list:
            self.info_textfield.insert(tk.END, info)
            self.info_textfield.insert(tk.END, '\n')
        self.info_textfield.see(tk.END)
        self.info_textfield.config(state=tk.DISABLED)

        c.desk_lamp()

    def magic_package(self):
        info_list = c.get_info_list('magic')
        self.info_textfield.config(state=tk.NORMAL)
        self.info_textfield.delete(1.0, tk.END)
        for info in info_list:
            self.info_textfield.insert(tk.END, info)
            self.info_textfield.insert(tk.END, '\n')
        self.info_textfield.see(tk.END)
        self.info_textfield.config(state=tk.DISABLED)
        c.magic_package()


class Controller:
    def __init__(self):
        self.model = Model()
        self.root = tk.Tk()
        self.root.config(cursor="none")
        # self.root.attributes('-fullscreen', True)
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

    def get_info_list(self, choice):
        return self.model.get_info_list(choice)


if __name__ == "__main__":
    c = Controller()
    # recorder = sr.Recognizer()
    # voice_thread = VoiceThread()
    # voice_thread.start()
    # phone_thread = PhoneThread()
    # phone_thread.start()
    c.run()
