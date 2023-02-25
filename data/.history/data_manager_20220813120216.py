import os


os.system("cat watchdog_5.txt | grep simple_sw >watchdog_5_1.txt")
os.system("cat watchdog_5_1.txt | grep 15012 >watchdog_5_2.txt")



