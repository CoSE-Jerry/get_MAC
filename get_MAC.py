import os
print("obtaining MAC Address...")
os.system("ifconfig -a | grep -Po 'wlan0     Link encap:Ethernet  HWaddr \K.*$' >> Mac.txt"
)
print("uploading file...")
os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload Mac.txt /pi_MAC")
print("operation complete...")        
