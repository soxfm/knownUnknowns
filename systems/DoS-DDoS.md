# Denial of Service vs Distributed Denial of Service Attack
### DoS vs DDoS
the easiest form of a DoS attack is one in which content is simoply requested from a site. this request will consume resources for both the person making it and the person being attack. in theory, if you have more bandwidth than the service you are attacking, you could consume their entire bandwith - meaning no ojne else would be able to download any files.

Some operations might be very resource intensive on the targeted server, but require little to no resources on the side of the attacker. Underprepared services make it cheap and easy for an attacker to slow down the server by overwhelming it, making the service unavailable to other users.

Most services, however, will limit the amount of resources spent on each visitor, to avoid a single user using up all its resources. The server might also block a user completely if their activity is deemed suspicious. In other cases a service might prompt for a captcha, to slow down automatic processes.
----
Defending against a Distributed Denial of Service Attack is more difficult. Instead of a single user with a single machine flooding a server with requests, there are thousands or even possibly millions of machines (botnets) making requests.

Botnets are ocmpromoised machines such as desktop computers, routers, servers and any other hardware connected to the internet(think IOT). The devices are infeceted with malware and remote controlled by a group of attackers; who often ren out these botnets on an hourly basis for the sole purpose of DDoS Attacks.
 
