import os
from ip import Ip

"""
 ip_range must be like that [first_ip, last_ip, range]
 what's range?! I mean if the first ip is 192.168.1.100 and last one is
 192.168.2.103 what's the x in last ip in this form ==> 192.168.1.x
 if we find x ==> 199 ==> ip_range will be like this: [192.168.1.100, 192.168.3.103, 199]
"""

def get_connected(ip_range:list):
    first = Ip(ip_range[0], ip_range[2])
    last = Ip(ip_range[1], ip_range[2])
    current = first
    while current <= last:
        pass
    
