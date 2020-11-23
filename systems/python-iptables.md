# Python Iptables using NFQUEUE
>> This target passes the packet to userspace using the nfnetlink_queue handler. The packet is put into the queue identified by its 16-bit queue number. Userspace can inspect and modify the packet if desired. Userspace must then drop or reinject the packet into the kernel.


> Forward all __INPUT__ packets to queue 1 with NNFQUEUE Targe
` iptables -A INPUT -j NFQUEUE --queue-num 1`
> Script to bind netfilter queue 1 and handle packets.
#!/usr/bin/python3

from netfilterqueue import NetfilterQueue
from scapy.all import *

def packetanalyzer(pkt):
    ip=IP(pkt.get_payload())
    if(ip.src=="192.168.122.1"):
        print(f"New packet from {ip.src}")
        pkt.accept()
    else:
	pkt.drop()

nfqueue=NetfilterQueue()
nfqueue.bind(1, packetanalyzer)
nfqueue.run()


Write your own port knocking script to secure ssh access
> DROP all ssh requests and send secret port requests to user-space with NFQUEUE target.
iptables -t filter -I INPUT -p tcp --dport 22 -j DROP
iptables -t raw -I PREROUTING -p tcp --sport 65534 --dport 65535 -j NFQUEUE --queue-num 1

> Capture packets from netfilter queue 1; check SRC-PORT and Secret-Port for Port Knocking and allow source to connect to ssh for the specified EXPIRETIME:
#!/usr/bin/python3

from os	import system
from netfilterqueue import NetfilterQueue
from scapy.layers.inet import IP
from time import time

SOURCEPORT=65534
SECRETPORT=65535
EXPIRETIME=30
ALLOWED={}

def portknocking(pkt):
    packet=IP(pkt.get_payload())
    currtime=time()
    for item in list(ALLOWED):
        if(currtime-ALLOWED[item] >= EXPIRETIME*60):
            del ALLOWED[item]
    if(packet.sport==SOURCEPORT and packet.dport==SECRETPORT and packet.src not in ALLOWED):
        print(f"Port {packet.dport} knocked by {packet.src}:{packet.sport}")
        system(f"iptables -I INPUT -p tcp --dport 22 -s {packet.src} -j ACCEPT")
        system(f"echo 'iptables -D INPUT -p tcp --dport 22 -s {packet.src} -j ACCEPT' | at now + {EXPIRETIME} minutes")
        ALLOWED[packet.src]=time()
        pkt.drop()

nfqueue=NetfilterQueue()
nfqueue.bind(1, portknocking)

try:
    nfqueue.run()
except KeyboardInterrupt:
    print("\nExit with Keyboard Interrupt")

> Knock on port and allow ssh connections from your computer
> NETCAT
`nc -p 65534 SERVER 65535`
