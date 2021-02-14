
# Raspberry Pi Cluster 
---
### Overview

 A cluster works by communication. A 'master' node is in charge of the cluster and the 'workers' are told what to do and to report back the results on demand. The best way to achieve this is by creating a wired intranet instance within a dedicated network. In order to maximize data throughput and effiency the cluster should have its own private subnet-link so that it can operate within a its own communication channel without hampering the overall bandwith of 'said' network. Thus, the use of both wired and wireless.

 ---

 ## SETUP
 ---
 ### BACKBONE

   The wired ethernet link is known as the cluster's 'backbone'. Since there will be no DHCP server to distribute addresses, the backbone should be manually configured on a different private subnet address in order to provide proper intracommunications. 

   **Network Configuration**
     ```bash
         $ sudo nano /etc/dhcpcd.conf
         $ interface eth0
         $ static ip_address=10.0.0.1/24

      For each subsequent node use the next number available from the master node. eg: 10.0.0.2/24. 
      Generate and copy ssh-keys to and from the master node to worker nodes. 

### Install MPI

**MPI** (Message Passing Interface):
  Protocol that allows multiple computers to delegate tasks among themselves and responde with results. Install MPI on each node of the cluster and their subsequent python bindings. 
  ```bash apt -y install mpich python3-mpi4py
  
  running  "mpiexec -n 1 hostname"

You should just get the name of the node echoed back at you. The -n means ‘how many nodes to run this on’. If you say one, it’s always the local machine

### Parallel computing

Time for our first cluster operation. From node1 (10.0.0.1), issue the following command:

mpiexec -n 4 --hosts 10.0.0.1,10.0.0.2,10.0.0.2,10.0.0.4 hostname

We’re asking the master supervisor process, mpiexec, to start four processes (-n 4), one on each host. If you’re not using four hosts, or are using different IP addresses, you’ll need to change this as needed. The command hostname just echoes the node’s name, so if all is well, you’ll get a list of the four members of the cluster. You’ve just done a bit of parallel computing!

### Multiplicity

In order for the cluster to work, each node needs to have an identical copy of the script we need to run, and in the same place. So, copy the same script to each node. Assuming the file is in your home directory, the quick way to do this is (from node1):

scp ~/prime.py 10.0.0.x:

Replace x with the number of the node required: scp (secure copy) will copy the script to each node. You can check this has worked by going to each node and running the same command we did on node1. Once you are finished, we are ready to start some real cluster computing.

### Compute

To start the supercomputer, run this command from the master (node1):

mpiexec -n 4 --host 10.0.0.1,10.0.0.2,10.0.0.3,10.0.0.4 python3 prime.py 100000

Each node gets a ‘rank’: a unique ID. The master is always 0. This is used in the script to allocate which range of numbers each node processes, so no node checks the same number for ‘primeness’. When complete, each node reports back to the master detailing the primes found. This is known as ‘gathering’. Once complete, the master pulls all the data together and reports the result. In more advanced applications, different data sets can be allocated to the nodes by the master (‘scattering’).
