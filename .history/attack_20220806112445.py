
import multiprocessing
import os 
import threading
import time
import sys
import random
import subprocess
import traceback
import tempfile
from more_itertools import distinct_permutations
import multiprocessing
import signal



class Attack_flow(threading.Thread):
    host_id=""
    dst_ip=""
    pid=0
    proc=None


    def __init__(self,host_id,dst_ip):
        threading.Thread.__init__(self)
        self.dst_ip=dst_ip
        self.host_id=host_id


    # def run(self):
    #     os.system("./host-cmd "+self.host_id+" hping3 -S -p ++ -i u10000 -d 2000 -V  "+self.dst_ip)


    # def run(self):
    #     os.system("./host-cmd "+self.host_id+" hping3 -S -p ++ -i u32000 -d 346 -V  "+self.dst_ip)  
    def run(self):
        cmd=self.host_id+" hping3 -S -p ++ -i u128000 -d 1546 -c 78 -V  "+self.dst_ip 
        os.system(cmd,shell=True)








def main():
    n=1
    attack_flow_arr=[]
    id_arr=[]
    last_id_arr=[]
    host_id_arr=["h01","h01","h11","h11","h12","h21","h21"]

    dst_ip_arr=["10.0.3.32","10.0.3.31","10.0.3.31","10.0.4.41","10.0.4.42","10.0.4.42","10.0.4.41"]

    for i in range(len(host_id_arr)):
        attack_flow=Attack_flow(host_id_arr[i],dst_ip_arr[i])
        attack_flow_arr.append(attack_flow)
    

    # time.sleep(10)
    # for i in range(1):
    #     attack_flow_arr[i].stop()

    print("where")


    while(True):
        id_arr=range(7)
        random.shuffle(id_arr)
        id_arr=id_arr[0:n]
        
        for id in range(7):
            if id in id_arr:
                attack_flow_arr[id]=Attack_flow(host_id_arr[id],dst_ip_arr[id])
        
            time.sleep(10)









if __name__ == "__main__":
    main()


