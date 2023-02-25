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

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
    def run(self, timeout):
        def target():
            print('Thread started')
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            print('Thread finished')
        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print('Terminating process')
            self.process.terminate()
            thread.join()
        print (self.process.returncode)



class Attack_flow():
    host_id=""
    dst_ip=""
    pid=0
    proc=None


    def __init__(self,host_id,dst_ip):
        self.dst_ip=dst_ip
        self.host_id=host_id



    def start(self):
        cmd="my_program & ./host-cmd "+self.host_id+" hping3 -S -p ++ -i u128000 -d 1546 -V  "+self.dst_ip  
        command = Command(cmd)
        command.run(timeout=3)






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
    
    for i in range(1):
        attack_flow_arr[i].start()


    print("where")


    while(True):
        last_id_arr=id_arr
        id_arr=range(7)
        random.shuffle(id_arr)
        id_arr=id_arr[0:n]
        
        for id in range(7):
            if id in last_id_arr:
                attack_flow_arr[id].start()
        
        time.sleep(10)









if __name__ == "__main__":
    main()


