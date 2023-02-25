import os
interval=5
file_name="watchdog"

file1_name="watchdog_"+str(interval)+".txt"

file2_name="watchdog_"+str(interval)+"_1.txt"


file3_name="watchdog_"+str(interval)+"_2"

file4_name="watchdog_"+str(interval)+"_3"
pid_arr=[15012,15027,15041,15083,15096,14997,15111,15059,14984]






os.system("cat "+file1_name+" | grep simple_sw > "+file2_name)


for pid in pid_arr:
    os.system("cat "+ file2_name +" | grep "+str(pid)+" > "+ file3_name+"_"+str(pid)+".txt")

for pid in pid_arr:
    os.system("cat "+ file3_name+"_"+str(pid)+".txt"+" | awk '{print $10}' > "+ file4_name+"_"+str(pid)+".txt")





