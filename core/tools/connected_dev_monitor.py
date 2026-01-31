import os
from ip import Ip

"""
 ip_range must be like that [first_ip, last_ip, range]
 what's range?! I mean if the first ip is 192.168.1.100 and last one is
 192.168.2.103 what's the x in last ip in this form ==> 192.168.1.x
 if we find x ==> 199 ==> ip_range will be like this: [192.168.1.100, 192.168.3.103, 199]
"""

def get_connected(ip_range:list):
    connected = []
    available = []
    first = Ip(ip_range[0], ip_range[2])
    last = Ip(ip_range[1], ip_range[2])
    current = first
    while True:
        command = f'ping {current.ip}'
        a = os.popen(command).read()
        if 'Sent' in a:
            print(f'{current.ip} owend\n'+'-'*20)
            connected.append(current.ip)
        else:
            print(f'{current.ip} is available\n'+'-'*20)
            available.append(current.ip)
        if current == last:
            return connected, available
        else:
            current = current.next()
            continue

print(get_connected(['192.168.1.2', '192.168.1.30', 199]))