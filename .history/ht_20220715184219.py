
import pyshark
import collections
import matplotlib.pyplot as plt
import numpy as np
 





# cap1 = pyshark.FileCapture('pcap/s0-eth5_in.pcap', only_summaries=True)
# cap2 = pyshark.FileCapture('pcap/s1-eth1_in.pcap', only_summaries=True)
# cap3 = pyshark.FileCapture('pcap/s1-eth2_in.pcap', only_summaries=True)
# cap4 = pyshark.FileCapture('pcap/s2-eth2_in.pcap', only_summaries=True)

# cap5 = pyshark.FileCapture('pcap/s4-eth5_in.pcap', only_summaries=True)
# cap6 = pyshark.FileCapture('pcap/s4-eth4_in.pcap', only_summaries=True)
# cap7 = pyshark.FileCapture('pcap/s3-eth4_in.pcap', only_summaries=True)


#cap = pyshark.FileCapture('pcap/s2-eth3_in.pcap', only_summaries=True)
dst_ip_arr = [
"10.0.9.1",
"10.0.1.11",
"10.0.1.12",
"10.0.2.21",
"10.0.2.22",
"10.0.3.31",
"10.0.3.32",
"10.0.4.41",
"10.0.4.42"]


attack_dst_ip_arr=["10.0.3.32","10.0.3.31","10.0.3.31","10.0.4.41","10.0.4.42","10.0.4.42","10.0.4.41"]

attack_src_ip_arr=["10.0.9.1","10.0.9.1","10.0.1.11","10.0.1.11","10.0.1.12","10.0.2.21","10.0.2.21"]

protocolList = [[],[]]
ipsrcList=[[],[]]
ipdstList=[[],[]]

cap_list=['pcap/s0-eth5_in.pcap','pcap/s1-eth1_in.pcap','pcap/s1-eth2_in.pcap','pcap/s2-eth2_in.pcap','pcap/s4-eth5_in.pcap','pcap/s4-eth4_in.pcap','pcap/s3-eth4_in.pcap','pcap/s3-eth5_in.pcap']

count=0
count_list=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for cap_name_id in range(len(cap_list)):
    flag=0
    cap = pyshark.FileCapture(cap_list[cap_name_id], only_summaries=True)
    if(cap_name_id<=3):
        flag=0
    else:
        flag=1
    for packet in cap:
        line = str(packet)
        formattedLine = line.split(" ")
        ipsrcList[flag].append(formattedLine[2])
        ipdstList[flag].append(formattedLine[3])
        protocolList[flag].append(formattedLine[4])



for i in range(len(ipsrcList)):
    for j in range(len(attack_dst_ip_arr)):
        if(ipsrcList[i]==attack_dst_ip_arr[j]and ipdstList[j]==attack_dst_ip_arr):




x_data=["flow1","flow2","flow3","flow4","flow5","flow6","flow7","flow8"]
 

x_width = range(0,len(x_data))
x2_width = [i+0.3 for i in x_width]

y_data=count_list
y2_data=count_list

plt.bar(x_width,y_data,lw=0.5,fc="r",width=0.3,label="attack_flow")
plt.bar(x2_width,y2_data,lw=0.5,fc="b",width=0.3,label="accept_attack_flow")
 
plt.xticks(range(0,8),x_data)



plt.ylabel("flow_count")
plt.xlabel("flow_name")
plt.savefig("result.png")


for count in count_list:
    print(count)


