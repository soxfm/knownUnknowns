# WPA Supplicant file
---

  touch /boot/wpa_supplicant.conf:
  insert configurations:

	```sh
		ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
		update_config=1
		country=US

		network={
		  ssid="WLAN SSID"
		  psk="wlan-ssid-presharedkey"
		}
	```


