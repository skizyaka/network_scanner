import scapy.all as sc

def scan(ip):
    arp_request = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = sc.srp(arp_request_broadcast, timeout=1)
    print(answered.summary)
#Узнать значение переменной   sc.ls(sc.ARP())
#   sc.arping(ip)


scan("Тут прописывается дипозон ip адресов")