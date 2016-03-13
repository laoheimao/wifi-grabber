from scapy.all import *
import os
from random import randint

unique_ssid = []
wifiX = 1  # lower bound of wifi card channel
wifiY = 14  # upper bound of wifi card channel


def Handler(pkt):
    if pkt.haslayer(Dot11):  # 802.11
        if pkt.type == 0 and pkt.subtype == 8:  # Beacon frame
            try:
                if pkt.info not in unique_ssid and len(pkt.info) > 0:
                    unique_ssid.append(pkt.info)  # append SSID name
                    unique_ssid.append(pkt.addr2)  # append corresponding mac address
                    signalStrength = -(256 - ord(pkt.notdecoded[-4:-3]))    # Decode RSSI value.
                                                                            # Might not work with all wifi cards.
                                                                            # Working ok with tplink WN7200ND
                    unique_ssid.append(signalStrength)
                    print unique_ssid
                    # print pkt.info
                    # print pkt.addr2
            except Exception, e:
                print str(e)


# sniff(iface="wlan1mon", count=0, prn=Handler,store=0)
currentChannel = wifiX
while currentChannel <= wifiY:
    print 'Current channel is %i' % currentChannel
    try:
        os.system('iw dev wlan1mon set channel %i' % currentChannel)
        sniff(iface="wlan1mon", count=0, prn=Handler, store=0, timeout=3)
    except Exception, e:  # Handle errors
        print str(e)
    currentChannel += 1
