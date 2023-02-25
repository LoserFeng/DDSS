
import pyshark
import collections
import matplotlib.pyplot as plt
import numpy as np
 





cap1 = pyshark.FileCapture('pcap/s0-eth5_in.pcap', only_summaries=True)
cap2 = pyshark.FileCapture('pcap/s1-eth1_in.pcap', only_summaries=True)
cap3 = pyshark.FileCapture('pcap/s1-eth2_in.pcap', only_summaries=True)
cap4 = pyshark.FileCapture('pcap/s2-eth2_in.pcap', only_summaries=True)

cap5 = pyshark.FileCapture('pcap/s4-eth5_in.pcap', only_summaries=True)
cap6 = pyshark.FileCapture('pcap/s4-eth4_in.pcap', only_summaries=True)
cap7 = pyshark.FileCapture('pcap/s3-eth4_in.pcap', only_summaries=True)
cap8 = pyshark.FileCapture('pcap/s3-eth5_in.pcap', only_summaries=True)

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

protocolList = []
ipsrcList=[]
ipdstList=[]

cap_list=['pcap/s0-eth5_in.pcap','pcap/s1-eth1_in.pcap','pcap/s1-eth2_in.pcap','pcap/s2-eth2_in.pcap']

cap_list.append(cap1)
# cap_list.append(cap2)
# cap_list.append(cap3)
# cap_list.append(cap4)
# cap_list.append(cap5)
# cap_list.append(cap6)
# cap_list.append(cap7)
# cap_list.append(cap8)



print(cap1[0])
for packet in cap1:
    print("where")
    print(packet)
    print("where1") 
    line = str(packet)
    formattedLine = line.split(" ")
    ipsrcList.append(formattedLine[2])
    ipdstList.append(formattedLine[3])
    protocolList.append(formattedLine[4])



counter = collections.Counter(protocolList)
 
plt.style.use('ggplot')



y_pos = np.arange(len(list(counter.keys())))
plt.bar(y_pos, list(counter.values()), align='center', alpha=0.5, color=['b', 'g', 'r', 'c', 'm'])   
plt.xticks(y_pos, list(counter.keys()))

plt.ylabel("Frequency")
plt.xlabel("Protocol Name")
plt.savefig("result.png")
