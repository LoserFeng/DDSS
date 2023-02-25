import os
interval=5
file_name="watchdog"

dir_name="./watchdog_"+str(interval)+"/"

file1_name="watchdog_"+str(interval)+".txt"

file2_name="watchdog_"+str(interval)+"_1.txt"

file2_name_pid="watchdog_"+str(interval)+"_pid_1.txt"

file3_name="watchdog_"+str(interval)+"_2"

file4_name="watchdog_"+str(interval)+"_3"



# 5 pid_arr=[15012,15027,15041,15083,15096,14997,15111,15059,14984]   
#pid_arr=[21867,21910,21894,21965,1,21923,21951,21980,21937]  
pid_arr=[]


os.system("mkdir "+file_name+"_"+str(interval))



os.system("cat "+file1_name+" | grep simple_sw > "+dir_name+file2_name)

os.system("cat "+dir_name+file2_name+" | awk '{print $2}' > "+dir_name+file2_name_pid)

file = open(dir_name+file2_name_pid,'r')


pid_array = file.readlines()

for pid in pid_array:
    if int(pid) not in pid_arr:
        pid_arr.append(int(pid))

print(pid_arr)




for pid in pid_arr:
    os.system("cat "+dir_name+ file2_name +" | grep "+str(pid)+" > "+dir_name+ file3_name+"_"+str(pid)+".txt")

for pid in pid_arr:
    os.system("cat "+dir_name+ file3_name+"_"+str(pid)+".txt"+" | awk '{print $10}' > "+dir_name+ file4_name+"_"+str(pid)+".txt")





