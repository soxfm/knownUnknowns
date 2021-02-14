----
title: usb-c gadget
date: 2021-02-14
category: [ "raspberry", "usb-c", "mods", "hardware", "configs" ]
----

# RPI as USB-C Gadget 
---
## Overview

Distributes power over usb-c connection to the rpi, network booting, data over usb-c. 
Initial Requirements : update the rpi bootloader. 

### Steps:

- add dtoverlay=dwc2 to /boot/config.txt
- add modules-load=dwc2 to the end of /boot/cmdline.txt
- touch /boot/ssh
- add 'libcomposite' to /etc/modules
- add denyinterfaces usb0 to /etc/dhcpcd.conf
- install dnsmasq 
- touch /etc/dnsmasq.d/usb

```bash
interface=usb0
dhcp-range=10.45.0.2,10.45.0.6,255.255.255.248,1h
dhcp-option=3
leasefile-ro
```

- create /etc/network/interfaces.d/usb0
```bash
auto usb0
allow-hotplug usb0
iface usb0 inet static
  address 10.45.0.1
  netmask 255.255.255.248
```

- create /root/usb.sh
```bash
#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p pi4
cd pi4
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
echo 0xEF > bDeviceClass
echo 0x02 > bDeviceSubClass
echo 0x01 > bDeviceProtocol
mkdir -p strings/0x409
echo "fedcba9876543211" > strings/0x409/serialnumber
echo "FM" > strings/0x409/manufacturer
echo "PI4 USB Device" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower
# Add functions here
# see gadget configurations below
# End functions
mkdir -p functions/ecm.usb0
HOST="00:dc:c8:f7:75:14" # "HostPC"
SELF="00:dd:dc:eb:6d:a1" # "BadUSB"
echo $HOST > functions/ecm.usb0/host_addr
echo $SELF > functions/ecm.usb0/dev_addr
ln -s functions/ecm.usb0 configs/c.1/
udevadm settle -t 5 || :
ls /sys/class/udc > UDC
ifup usb0
service dnsmasq restart
```

- chmod +x /root/usb.sh
- edit /etc/rc.local > tee -a /root/usb.sh


