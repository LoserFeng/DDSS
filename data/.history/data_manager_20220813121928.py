import os
interval=5
file_name="watchdog"

file1_name="watchdog_"+str(interval)+".txt"

file2_name="watchdog_"+str(interval)+"_1.txt"


file3_name="watchdog_"+str(interval)+"_2.txt"

pid_arr=[1,2,3,4,5,6,7]






os.system("cat watchdog_5.txt | grep simple_sw >watchdog_5_1.txt")


for pid in pid_arr:
    os.system("cat watchdog_5_1.txt | grep "+str(pid)+" >watchdog_5_2.txt")

for pid in pid_arr:
    os.system("cat watchdog_5_2.txt | awk '{print $10}' > "+ file_name+"_"+str(interval)+"_"+str(pid)+".txt")





