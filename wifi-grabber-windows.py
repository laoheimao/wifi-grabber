######################################
##
## Initially written as a part of the pyGeolocation project but has more functionality here.
##
######################################

import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "all"]) # netsh command. Try it on CMD to examine the output

results = results.replace("\r", "")
ls = results.split("\n")  # Splitting the result of our netsh command into a list containing each line

ssids = []
x = 0  # For traversing ls
while x < len(ls):
    if ls[x].split(" ")[0] == 'SSID':  # When we reach a line which lists properties about a certain SSID
        ssid = ls[x].split(': ')[1]  # Wifi name
        print ssid

        networkType = ls[x+1].split(': ')[1]  # Network type
        print networkType

        authentication = ls[x+2].split(': ')[1]  # WPA type
        print authentication

        encryption = ls[x+3].split(': ')[1]  # Encryption type
        print encryption

        bssid = ls[x+4].split()[3]  # MAC Address
        print bssid

        signal = ls[x+5].split()[2].split('%')[0]  # Signal strength in percentage
        rssi = (int(signal)/2) - 100  # RSSI value
        print rssi

        radioType = ls[x+6].split(': ')[1]  # Radio type
        print radioType

        channel = ls[x+7].split(': ')[1]  # WiFi channel
        print channel

        basicRates = ls[x+8].split(': ')[1]
        print basicRates

        otherRates = ls[x+9].split(': ')[1]
    x += 1
