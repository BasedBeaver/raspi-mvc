import os

ret = os.system("ping -c 3 -W 3000 192.168.0.102")
if ret != 0:
    print("Offline")
else:
    print("Online")
