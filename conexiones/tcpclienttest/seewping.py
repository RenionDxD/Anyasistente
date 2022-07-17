import ipaddress
import os
import socket


#ip address string must be in unicode to use ipaddress module
def seew(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    id = s.getsockname()[0]
    s.close()
    #return id
    cmd = 'ifconfig wlo1 | grep "inet"'
    texto  = os.system(cmd)
    ids = id.rindex('.')
    id = id[0:ids]+".0/24"
    print(id)
    network = ipaddress.ip_network(id)

    print("Running Python ping sweep of target IP range 10.11.1.0/24")

    for i in network.hosts():
        str(i)
        response = os.system("ping %s -c 1 > /dev/null" %i)
        
        if response == 0:
                    print("%s UP" %i)
        else:
                    print("%s No response" %i)

    print("Ping sweep complete")


if __name__ == '__main__':
    seew()