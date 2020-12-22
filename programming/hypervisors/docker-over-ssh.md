---
title: docker over ssh
slugs: docker-over-ssh
tag_list: [ 'code', 'programming', 'docker', 'hypervisors', 'servers', 'sbc' ]
date: 2020-12-21
---

### Creating a Cloud VM and Using Docker Build

ssh into the machine and install docker
```bash
curl -SLsf https://get.docker.com | sudo sh
```

Add a user which makes use of Docker and which can log into the machine remotely.
```bash
useradd build -G docker -m -S /bin/bash
```

Copy ssh-public key info for the user
```bash
sudo -u build mkdir -p /home/build/.ssh
cp /root/.ssh/authorized_keys /home/build/.ssh/
chown -R build:docker /home/build/.ssh
```

### Docker Daemon
```bash
docker -H ssh://build@xyz.xyz.xyz.xyz:22 info
Client: Docker Engine - Community

