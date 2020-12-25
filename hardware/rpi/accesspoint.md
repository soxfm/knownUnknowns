## Installation

**Preparation**

The first step is, obviously, to install the image onto the uSD Card and booting it up. The first boot usually takes longer than a normal startup because the Pi has to do first time stuff like generating new SSH keys and so on.

Then use `sudo raspi-config` to configure the Pi to your likings.

Now update it using `sudo apt update && sudo apt full-upgrade` - once it's done reboot it and we'll start with the actual AP installation.

**AP setup**

Firstly, install hostapd and bridge-utils with the following command.
```
sudo apt install hostapd bridge-utils
```

Now comes the important part. The next step is editing the hostapd.conf.
```
sudo nano /etc/hostapd/hostapd.conf
```

If the file is not empty just delete it's content. We will be using a custom config anyways. The minimal config that you should use looks like that:
```
# Bridge mode
bridge=br0

# Networking interface
interface=wlan0

# WiFi configuration
ssid=RouteryPi
channel=1
hw_mode=g
country_code=US
ieee80211n=1
ieee80211d=1
wmm_enabled=1

# WiFi security
auth_algs=1
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=SomeStrongPassword
```
Just paste the text into the hostapd config file, edit `country_code=US` to your country, save it and you're good to go.
You should then update `wpa_passphrase` to your custom WiFi password and optionally `channel` to another WiFi channel.

To create and use the network bridge we only have to edit one more file. Now edit the network interfaces file like that:
```
sudo nano /etc/network/interfaces
```

Delete anything that's in here and paste the following configuration:
```
auto lo
iface lo inet loopback

# Ethernet
auto eth0
allow-hotplug eth0
iface eth0 inet manual

# WiFi
auto wlan0
allow-hotplug wlan0
iface wlan0 inet manual
wireless-power off

# Bridge
auto br0
iface br0 inet dhcp
bridge_ports eth0 wlan0
bridge_fd 0
bridge_stp off
```
This will result in the Pi using DHCP which means it can be used in **any existing** network. The downside of this is that you have to find out the IP address if you want to, let's say, use SSH. You could use a static IP address by changing the **br0**(!) interface config a little bit - just google 'static ip raspberry pi'. (For the lazy: https://duckduckgo.com/?q=static+ip+raspberry+pi)

**Final steps**

After you did a quick reboot using `sudo reboot`, you can start testing the whole thing. To test the hostapd config use this command: `sudo hostapd /etc/hostapd/hostapd.conf`. Note: If it does exit without you doing something, then there is something wrong with it. To go into debug mode use `sudo hostapd -dd /etc/hostapd/hostapd.conf`.

While testing the hostapd config you can also try connecting as a client. If you've done everything correctly you should be able to do so without any problems.

To enable hostapd to run upon boot you have to edit one last file.
```
sudo nano /etc/default/hostapd
```

Now paste this text into the file and save it:
```
RUN_DAEMON=yes
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

You're ready to go! From now on hostapd will start whenever your Pi boots up.

## Autostart issue

Some users reported issues with the above mentioned method of autostarting hostapd. From hostapd's side this should all work, but for some reason it looks like Raspbian doesn't like that anymore. The latest workaround is to paste the following commands to overwrite Raspbian's default masking of hostapd. See issue #5 for more info.

```sh
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
```


## Speed

I did some speed tests with my Raspberry Pi 4 and I have to admit I'm still very disappointed. Although the Pi features dual band wifi and gigabit ethernet the speeds really aren't outstanding.
Maybe I did something wrong, however the fact that it's working leads me to believe that these results are what you get...

If you get different speed results, please let me know.

**2.4 GHz Test Router VS Pi:**
