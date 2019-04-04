# Writeup 6 - Forensics

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 Pts)
1. The ip was 142.93.136.81. I found this using Wireshark by looking at the ip addresses, finding a get request from the ip address above, and seeing that the destination of the http was to the client.

2. The user is using command injections to get into the file system. I found this by looking through the data in wireshark and find a bunch of commands being entered the packet data. After following the tcp stream and seeing what the data contained, I saw the Username and Password being entered as well as the phrase, “PORT command successful” This implies that the user used a command injection to get into the file system to steal files as we can see in the later packet transfers. vsFTPd 3.0.3 is a tool I found by following one of the streams that was transferring data from the server and seeing vsFTPd on the first line. The lines following it are commands to retrieve data and store it.

3. The hackers ip is 159.203.113.181. I found this by looking at ip’s different from the website’s ip on wireshark. Using the ip address found above, I looked at transmission of data with the server and other ip addresses. One of the packets with greetz.fpff had a destination of 159.203.113.181. There were some other ip’s that communicated with the server however, they were not doing malicious activities (for example one ip called a get request on the server). To find the location of the hacker, I went to iplocation.net, entered the ip and found that the hacker was located in Clifton, New Jersey.

4. They are using port 20. Using wireshark, I looked at the packets that contained the transfer of the greetz.fpff file and the find_me.jpeg file. I then clicked each packet and looked at the source and destination ports. In both cases, the user used port 20 to receive and transfer data with the server.
5. 
    A. I followed the tcp stream find_me.jpeg and downloaded the binary version of it. I know they stole the file as one of the packets has a RECV command on the image. I then used exiftool on my virtual machine on the binary file and got a bunch of info on the photo. The file type is a JPEG image. Additionally, on Wireshark, the description states the file as find_me.JPEG.

    B. The photo was taken at La Mano, in Punta del Este (Brava Beach), Uruguay. I took the binary file that I downloaded from the previous question and opened it, leaving me with a photo of a beach and a hand in the sand. I searched it up “hand in the sand” and it returned the location with similar photos of the hand.

    C. The photo was taken on 12/23/2018. The metadata says “Create Date: 2018:12:23 17:16:24.002.” Also on the properties of the photo, it says the photo was taken on Sunday. I found this using exiftool and calling it on the .jpeg file.

    D. After following the tcp stream on one of the requests that had ‘(RETR find_me.jpeg)’, I saw the words “Apple iPhone 8 back camera.” To confirm this, I used exiftool and saw that the lens model said the same as above.

E. Using exiftool, the photo was taken 4.5 meters below sea level.

6. The hackers left a file called greetz.fpff on the server. I found this through wireshark after seeing a STOR greetz.fpff call from the source to the server. The destination was to the server as well, confirming that the file was going to the server.

7. A strong countermeasure is to invest in a firewall. A firewall’s main function is to filter out information leaving and going from a server and/or computer. This works because the server can prevent any unwanted access of files as well as transferring files to and from the server. 


### Part 2 (55 Pts)

SUMMARY OF CODE: Using the stub code, I got an understanding of how bytes are read in from the file using unpack. However, I wasn’t sure what the “<LL” meant in the unpack function. So, looked up the documentation and found all of the possible ways to get a specific input from the unpack function. Next, I added the code to find the remaining elements in the header using the stub code provided as help. Moving on to the body, I used a for loop with 5 iterations: the 5 came from the value found from the header. After this, I read in 8 bytes, the first 4 being the type and the last were the length of the data. Using this, I checked all type cases and wrote code to unpack each one.

I. The file was generated on 03-27-2019 at 4:15:05 (24 hour time). To figure this out, I developed a parser that followed the fpff guidelines and read in binary data to see what the data was in plaintext. I opened the fpff file using ‘open’ and read in exactly 8 bytes, which were split into two 4 byte values, and stored the conversion to ascii (from unpack) in 2 variables: MAGIC & VERSION. Next, I read in another 8 bytes, however this time, I only used the first 4 bytes to find the timestamp as the specification declared it as 1 word, which is 4 bytes. The problem was that the data returned was simply a large number that was not in the correct Unix time format. To convert it to UTC, I imported datetime and called the function ‘datetime.utcfromtimestamp(time) using the value unpack returned as the parameter to the the statement above (time). Next I had to convert it to a string readable time so I called strftime and passed in the correct format to get the desired date and time.

II. The author is ‘flinch’. Using the parser I first unpacked the first 4n (where n is a constant) bytes that represented the magic bytes, version, and timestamp. Then, I moved the offset by another 4 bytes to see what the author was. The data returned was in a tuple, so I called decode(“utf-8”) on author[0] to remove the ‘b’ leading the data.

III. I ADDED AN IMAGE CALLED OUTPUT.PNG IN THE WRITEUP DIRECTORY. THAT HAS THE ANSWER TO THIS QUESTION

IV. 	R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC. For this flag, I followed the tcp stream that had the greetz.fpff file being transferred. After opening the file, I scrolled down and found the tag on the last line. I also found the same tag another way by implementing the parser and running it on the greetz.fpff file. Once  I got to section 7 the data printed out the flag. 
Another flag I found was CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak}, which I found through implementing the .png part of the parser. I opened a new .png file, wrote the signature of a png to it, and wrote the remaining data given from the fpff file to the png file. After opening the file, I was left with a picture with testudo and a flag next to it.



