# Initial Setup script for rpi
---

## Basic tools

```bash
sudo apt -y install build-essential libtool autoconf automake make libtool ufw apt-utils apt-transport-https man-db tldr python3-pip curl wget bison flex whois dnsutils speedtest-cli neofetch screenfetch fzf vim neovim python3-pip htop nano git git-extras dirmngr autoconf automake make libtool xz-utils unzip zip tldr python3-pip net-tools dnsutils nmap inetutils-tools tcpdump wicd-curses && sudo apt update -y && sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt dist-upgrade -y && sudo apt-get autoremove -y &&sudo apt-get clean -y && sudo apt-get autoclean -y
```

### Install Additional Packages
```bash
# install node
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
$ sudo apt -y install node js 
# install rust
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# install Docker
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo ./get-docker.sh


# Optional (rust learning repository)
$ git clone https://github.com/second-state/wasm-learning.git
```