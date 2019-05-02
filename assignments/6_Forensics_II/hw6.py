#!/usr/bin/env python2

import sys
import struct
from datetime import datetime
import re

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

png_count = 0 
gif_count = 0
# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

offset = 0
magic, version= struct.unpack("<LL", data[offset:offset+8])
offset += 8
time_stamp, _ = struct.unpack("<LL", data[offset:offset+8])
offset += 4
author = struct.unpack("8s", data[offset:offset+8])
offset += 4
_,section_count = struct.unpack("<LL", data[offset:offset+8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
time = int(time_stamp)
print("TimeStamp: " + datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'))
print("Author: '{0}'".format(author[0].decode("utf-8")))
print("Section Count: %d" % int(section_count))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
offset += 8
slen = 1
section_num = 1
to_print = ""
for x in range(section_count) :
    print("Section %d" % (section_num))

    stype, slen = struct.unpack("<LL",data[offset:offset+8])
    counter = slen/4
    offset+=8
    print(" length: %d" %(slen))
    if (stype == 1):
        print("ASCII")
        string = str(slen) +"s" 
        s = struct.unpack(string,data[offset:offset+slen])
        print(s[0].decode("utf-8"))
        offset += int(slen)
    
    if (stype == 2):
        to_print = ""
        print("UTF8")
        for i in range(offset,offset + int(slen), 8):
            s,sc = struct.unpack("<LL",data[offset:offset+int(slen)])
            combined = int(str(s) + str(sc))
            to_print += (combined.decode('hex').decode('utf-8'))
        offset +=  int(slen)
    
    if (stype == 3):
        to_print = ""
        print("WORDS")
        for i in range(int(slen)/4):
            s = struct.unpack("s", data[offset: offset + 4])
            to_print += s[0].decode("utf-8")
            offset += 4
        print(to_print)
    if (stype == 4):
        to_print = ""
        print("DWORDS")
        for i in range(int(slen)/8):
            s = struct.unpack("S", data[offset:offset+8])
            print += s[0].decode("utf-8")
            offset += 8      
    if (stype == 5):
        to_print = ""
        print("DOUBLES")
        for i in range(int(slen)/8):
            s = struct.unpack("S", data[offset:offset+8])
            print += s[0].decode("utf-8")
            offset += 8     
        
    if (stype == 6):
        if (slen != 16):
            bork("slen not 16")
        print("COORD")
        s,sc = struct.unpack("dd",data[offset:offset+16])
        offset += 16
        print("(%f,%f)" % (s,sc))

    if (stype == 7):
        if (slen != 4):
            bork("invalid section ref")
        print("REFERENCE")
        s = struct.unpack("S", data[offset:offset+4])
        offset += 4
        to_print = ""
        to_print += s.decode("utf-8")
        print(to_print)

    if (stype  == 8):
        png_count += 1
        tmp_str = str(png_count) + ".png"
        print("PNG")
        with open(tmp_str,  "wb") as f:
            f.write(bytes([137,80,78,71,13,10,26,10]))
            l = struct.unpack(str(slen)+"s",data[offset:offset + slen])
            f.write(l[0])
        offset += int(slen)
    if (stype == 9 ):
        gif_count += 1
        print("GIF87")
        tmp_str =str(gif_count) + ".gif"
        with open(tmp_str, "wb") as f:
            f.write(bytes(("GIF87a").encode('utf8')))
            g = struct.unpack(str(slen)+"s", data[offset:offset + slen])
            f.write(g[0])
        offset += int(slen)
    section_num += 1 
   
    if (stype == 10):
        gif_count += 1
        print("GIF89")
        tmp_str =str(gif_count) + ".gif"
        with open(tmp_str, "wb") as f:
            f.write(bytes(("GIF89a").encode('utf8')))
            l = struct.unpack(str(slen)+"s",data[offset:offset + slen])
            f.write(l[0])
        offset += int(slen)
    

        


    

    