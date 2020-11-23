# Linux Security Notes

## IpTables
%% compiled from several sources including:
%% https://major.io's iptables' best practices.
%% https://github.com/trimstray/iptables-essentials
#### Intro: Understanding how iptables fully match packets with chains and rules.
1. IPTable's Rules are read from top to bottom.
2. If No matching rule is found the default policy of the chain will be applied
3. Create a DROP or Reject Rule before the `commit`  section of the iptables main.conf file.
4. Flushing iptables chain's is a no-no __avoid, blindly__ `iptables -F`
5. Remember lo0: many (especially critical/internal applications) require usage of the default loopback interface. Ensure that you set  up your rules carefully so that traffic may pass unobstructed on lo0 interface.
6. Combine Rule Groups into Separate Chains: "If you have a certain subset of rules that may be a little complicated, consider breaking them out into their own chain. You can just add in a jump to that chain from your default set of chains."
7. Use **Reject** until proper setup of rules has been verified. __Packet rejects generates echo requests which can be observable by the user and adjusted accordingly.__
8. Document and Comment your Code, especially when using specific rules for certain ports/addresses.
 
#### General Rules:
These commands are geared towards debian-based operating systems.
	netfilter-persistente save 			# saves current iptables ruleset
	iptables -n -L -v 					# verbose list of active rulesets
	iptables -n -L -v --line-numbers	# verbose listing with added line numbering
	iptables -S							# print out all active rulesets
	iptables -L INPUT					# list rules for INPUT Chain
	iptables -S INPUT					# print rule specification for INPUT Chain
	iptables -L INPUT -v				# show packet counts and aggregate Size
	iptables -D INPUT 10				# Delete rule by chain & Number
	
Delete Rule by Specification:`iptables -D INPUT -m conntrack --ctstate INVALID -j DROP`

Flush All Rules, Delete All Chains, and Accept All
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X

Insert New Firewall rule:
`iptables -I INPUT 2 -s 202.54.1.2 -j DROP`

Allow Connections to Loopback Interface lo0
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
Allow Established and Related Connections
`iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT`

Pass traffic from internal (eth1) to external(eth0) interface
`iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT`
Drop Invalid Packets
`iptables -A INPUT -m conntrack --ctstate INVALID -j DROP`
Block a specific IP Address or Block and issue a Rejection response
`iptables -A INPUT -s 192.168.x.x -j DROP`
`iptables -A INPUT -s 192.168.x.x -j REJECT`

Block connections to __ethernet0__ NIC:
`iptables -A INPUT -i eth0 -s 192.168.252.10 -j DROP`

Allow incoming SSH Connections
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
Or
Only allow incoming ssh connections from specified IP Address/Subnet
iptables -A INPUT -p tcp -s 192.168.240.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT

Allow ssh  out
iptables -A OUTPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT

Block outgoing misused services/dated protocols
iptables -A OUTPUT -p tcp --dport 25 -j REJECT # SMPT
iptables -A OUTPUT -p tcp --dport 136 -j REJECT # NetBios
iptables -A OUTPUT -p tcp --dport 137 -j REJECT
iptables -A OUTPUT -p tcp --dport 138 -j REJECT
iptables -A OUTPUT -p tcp --dport 139 -j REJECT
iptables -A OUTPUT -p tcp --dport 23 -j DROP # Telnet
iptables -A OUTPUT -p tcp --dport 445 -j DROP # Microsoft 
iptables -A OUTPUT -p tcp --dport 110 -j DROP # POP3

Drop Packets related to Private Subnets(LAN) on a Public Face Interface(WAN)
iptables -A INPUT -i eth0 -s 192.168.0.0/24 -j DROP
iptables -A INPUT -i eth0 -s 10.0.0.0/8 -j DROP
iptables -A INPUT -i eth0 -s 172.16.0.0/16 -j DROP


Drop Packets from specific MAC Addresses:
iptables -A INPUT -m mac --mac-source 00:0X:0X:AX:CX:BX -j DROP
iptables -A INPUT -p tcp --destination-port 22 -m mac --mac-source 00:0X:0X:AX:CX:BX -j DROP

Block ICMP Echo Responses
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
iptables -A INPUT -i eth0 -p icmp --icmp-type echo-request -j DROP

Query radb servers for facebook network services; then block all outgoing traffic to facebook servers:
for i in $(whois -h whois.radb.net -- '-i origin AS32934' | grep "^route:" | cut -d ":" -f2 | sed -e 's/^[ \t]*//' | sort -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | cut -d ":" -f2 | sed 's/$/;/') ; do

  iptables -A OUTPUT -s "$i" -j REJECT

done 
Log and Drop Packets
iptables -A INPUT -i eth1 -s 10.0.0.0/8 -j LOG --log-prefix "IP_SPOOF A: "
iptables -A INPUT -i eth1 -s 10.0.0.0/8 -j DROP

# block multiple services 
iptables -A INPUT -i eth0 -p tcp -m state --state NEW -m multiport --dports ssh,smtp,http,https -j REJECT # or DROP

restrict number of connections:
iptables -A FORWARD -m state --state NEW -p tcp -m multiport --dport http,https -o eth0 -i eth1 \
    -m limit --limit 20/hour --limit-burst 5 -j ACCEPT

iptables -A INPUT -p tcp -m state --state NEW --dport http -m iplimit --iplimit-above 5 -j DROP
Save List of recent Connections to match against table
iptables -A FORWARD -m recent --name portscan --rcheck --seconds 100 -j DROP
iptables -A FORWARD -p tcp -i eth0 --dport 443 -m recent --name portscan --set -j DROP
Restrict traffic specific to a certain **'string'** value
iptables -A FORWARD -m string --string '.com' -j DROP
iptables -A FORWARD -m string --string '.exe' -j DROP
iptables -A FORWARD -m string --string '.sql' -j DROP
iptables -A FORWARD -m string --string '.whois' -j DROP
iptables -A FORWARD -m string --string '.nmap' -j DROP
iptables -A FORWARD -m string --string '.rpc' -j DROP

Rules Constraint to Certain Time periods:
iptables -A FORWARD -p tcp -m multiport --dport http,https -o eth0 -i eth1 \
    -m time --timestart 21:30 --timestop 22:30 --days Mon,Tue,Wed,Thu,Fri -j ACCEPT

Protect Against Port Scanning
iptables -N port-scanning
iptables -A port-scanning -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s --limit-burst 2 -j RETURN
iptables -A port-scanning -j DROP

BruteForce Protection on destination port 22 (SSH)
iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --set
iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --update --seconds 30 --hitcount 5 -j DROP

Reject based on specified TTL values
`iptables -A INPUT -s 1.2.3.4 -m ttl --ttl-lt 40 -j REJECT`

SYNFLOOD Protection:
iptables -N syn_flood

iptables -A INPUT -p tcp --syn -j syn_flood
iptables -A syn_flood -m limit --limit 1/s --limit-burst 3 -j RETURN
iptables -A syn_flood -j DROP

iptables -A INPUT -p icmp -m limit --limit  1/s --limit-burst 1 -j ACCEPT

iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 1 -j LOG --log-prefix PING-DROP:
iptables -A INPUT -p icmp -j DROP

iptables -A OUTPUT -p icmp -j ACCEPT

Recheck Fragmented Packets
`iptables -A INPUT -f -j DROP`

Block Bogus MSS Values
`iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP`

Drop all Null Valued Packets
`iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP`

Block Packets which are being sent from Private Subnet Addresses(includes .local mcast)
_subnets=("224.0.0.0/3" "169.254.0.0/16" "172.16.0.0/12" "192.0.2.0/24" "192.168.0.0/16" "10.0.0.0/8" "0.0.0.0/8" "240.0.0.0/5")

for _sub in "${_subnets[@]}" ; do
  iptables -t mangle -A PREROUTING -s "$_sub" -j DROP
done
iptables -t mangle -A PREROUTING -s 127.0.0.0/8 ! -i lo -j DROP

View Logs:
`tail  -f /var/log/messages`
`grep 'IP SPOOF' /var/log/messages`

