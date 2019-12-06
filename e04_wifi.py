from time import sleep
import network
import ubinascii

station = network.WLAN(network.STA_IF)
accesspoint = network.WLAN(network.AP_IF)

network = ({'ssid':'micropython','password':'PyAmsterdam'},
           {'ssid':'test', 'password':'testtest'}
          )



def scan_networks():
    aps     = station.scan()
    print('network                         channel signal security    hidden  mac')
    for ap in aps:
        ssid = ap[0].decode('utf-8')
        mac = ubinascii.hexlify(ap[1]).decode('utf-8').upper()
        mac = ':'.join(mac[i*2:i*2+2] for i in range(len(mac)//2))
        channel = ap[2]
        signal = ap[3]
        auth = ('open', 'WEP', 'WPA-PSK', 'WPA2-PSK', 'WPA/WPA2-PSK','')[ap[4]]
        vis = ('visible', 'hidden')[ap[5]]
        print('{:32} {:>6} {:>5} {:12} {:7} {}'.format(ssid,ap[2],ap[3],auth,vis,mac))




def scan_and_connect(networks = network ):
    station.active(True)
    print()
    print('scanning network')
    stations_ssid = []
    while len(stations_ssid) == 0:
        stations_ssid = list(str(net[0],'utf-8') for net in station.scan())
        print('.', end='')
        sleep(0.2)
    print()
    print('found networks:', ', '.join(stations_ssid))

    for net in networks:
        if 'ssid' in net and 'password' in net:
            ssid = net['ssid']
            psk = net['password']

            if ssid in stations_ssid:
                station.connect(ssid,psk)
                print('connecting to wifi network {}'.format(ssid))
                print('deactivating accespoint mode')
                accesspoint.active(False)

    print('getting ip adress')
    ip_adress = '0.0.0.0'
    while ip_adress == '0.0.0.0':
        ip_adress = station.ifconfig()[0]
        sleep(0.2)
        print('.', end='')
    print()
    ips = station.ifconfig()
    print(' IP adress {}\n netmask   {} \n gateway   {} \n dns       {}'.format(*ips))
    print()





def config_ap(ssid = 'Hello PyAmsterdam', pwd = 'terrible_88', active = False):
    accesspoint.config_ap(essid = ssid)
    accesspoint.config_ap(password = pwd)
    accesspoint.active(active)
