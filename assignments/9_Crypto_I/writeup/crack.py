#!/usr/bin/env python3

import hashlib
import string
import os
import sys

def crack():
    hashes = open("hashes.txt","r").readlines()# open and read hashes.txt
    passwords = open("passwords.txt","r").readlines()# open and read passwords.txt
    characters = string.ascii_lowercase
  
    for c in characters:
        for p in passwords:
            # print(p)
            call = c + p
            call = call.rstrip()
            x = hashlib.sha256(call.encode("ascii")).hexdigest()
            #print(call + " ----> " + x)
            for h in hashes:
                if h.rstrip() == x:
                    print(call + " ----> " + x)
            # crack hashes
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()