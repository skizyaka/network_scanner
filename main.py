import scapy.all as sc

def scan(ip):
    arp_request = sc.ARP(pdst=ip)
    arp_request.show()
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()
#Узнать значение переменной   sc.ls(sc.ARP())
#   sc.arping(ip)


scan("Тут прописывается дипозон ip адресов")