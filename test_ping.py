import os

ret = os.system("timeout 0.5 ping -c 1 192.168.0.102")
if ret != 0:
    print("Offline")
else:
    print("Online")
