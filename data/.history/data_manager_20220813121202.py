import os

file_name="watchdog"
file1_name="watchdog_5.txt"

file2_name="watchdog_5_1.txt"


pid_arr=[1,2,3,4,5,6,7]

os.system("cat watchdog_5.txt | grep simple_sw >watchdog_5_1.txt")
os.system("cat watchdog_5_1.txt | grep 15012 >watchdog_5_2.txt")

os.system("cat watchdog_5_2.txt | awk '{print $10}' > " watchdog_)





