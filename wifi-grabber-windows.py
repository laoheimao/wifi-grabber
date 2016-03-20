import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "all"]) # netsh command. Try it on CMD to examine the output

results = results.replace("\r", "")
ls = results.split("\n")  # Splitting the result of our netsh command into a list containing each line

ssids = []
x = 0  # For traversing ls
while x < len(ls):
    if ls[x].split(" ")[0] == 'SSID':  # When we reach a line which lists properties about a certain SSID
        ssidLine = ls[x]
        ssidLineSplit = ls[x].split(': ')
        ssid = ssidLineSplit[len(ssidLineSplit)-1]
        print ssid

        bssidLine = ls[x+4]
        bssidLineSplit = ls[x+4].split()
        bssid = bssidLineSplit[len(bssidLineSplit)-1]
        print bssid

        signalLine = ls[x+5]
        signalLineSplit = ls[x+5].split()
        signal = signalLineSplit[len(signalLineSplit)-1]
        signal = int(signal[:len(signal)-1])
        print signal

    x += 1
