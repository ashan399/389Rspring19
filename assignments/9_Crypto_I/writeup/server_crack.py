#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes =open("hashes.txt","r").readlines() # open and read hashes.txt
    passwords = open("passwords.txt","r").readlines()# open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58 1337'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    print(data)
    data = data.split()
    data = data[5].decode('ascii')
    print("")
    print("")
    print("")
    print(data)
    print("")
    print("")
    print("")
    count = 0
    while(count < 3):
        for c in characters:
            for p in passwords:
            # print(p)
                call = c + p
                call = call.rstrip()
                x = hashlib.sha256(call.encode("ascii")).hexdigest()
                print(call + " ----> " + x)
                if x == data:
                    if count == 2:
                        s.send(str.encode(call +"\n"))
                        time.sleep(1)
                        d = s.recv(1024)
                        print(d)
                        return
                    if count == 1:
                        s.send(str.encode(call +"\n"))
                        time.sleep(1)
                        d = s.recv(1024)
                        print(d)
                        data = d.split()
                        data = data[3].decode('ascii')
                        print(data)
                        time.sleep(1)
                        count += 1

                    if count == 0:
                        s.send(str.encode(call +"\n"))
                        time.sleep(1)
                        d = s.recv(1024)
                        print(d)
                        data = d.split()
                        data = data[4].decode('ascii')
                        print(data)
                        time.sleep(1)
                        count += 1
                    
                

    # data = s.recv(1024)
    # print(data)
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()