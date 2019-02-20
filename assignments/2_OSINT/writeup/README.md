# Writeup 2 - OSINT

Name: *Ashan Panduwawala*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Ashan Panduwawala

## Assignment Writeup

### Part 1 (45 pts)

1. v0idcache’s real name is Elizabeth Moffet. I found this after searching up her username on inteltechniques and getting a hit on twitter. 
2. She is a banking CEO at 1137bank.money. The details of her work were in her twitter bio. http://1337bank.money/
3. Her email is v0idcache@protonmail.com. I found it on the about tab of her website which was on her twitter. She also has a twitter with the username: v0idcache. She also uses pastebin which I found using inteltechniques.
4. I went on security trails and pasted the domain of the website. The results returned with an ip address of 142.93.136.81. With this ip, I went to iplocation.net and found that the ip was located in Amsterdam City, Netherlands.
5. I added robots.txt to the end of the url and found the directory name: /secret_directory.
6. On kali, I ran nmap on the ip address and scanned all 60000+ ports. I got 3 ports 22, 80, 1337. Port 22 is runnning on ssh, port 80 is running on http, and port 1337 is running on waste.
7.
8. On the bank website, I did inspect element and found the phrase <!-- Good find! CMSC389R-{h1dd3n_1n_plain_5ight} --> in the HTML. I also added robots.txt to the url and found a secret directory. After adding the directory to the url, I got the tag : CMSC389R-{h1ding_fil3s_in_r0bots_L0L}. I also found one using centralops.net and entering the url of her website; Under DNS records, there is a text  field saying "CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}". 



### Part 2 (75 pts)
For this part, I modified the python stub code to enter all possible passwords into the server. Since I had an idea of the username (v0idcache), I was able to try every possible password combination on the server using a txt file called rockyou.txt. Everytime I tried a password I would see if the data returned was a success. Since going through each password one by one was slow, I modified the program to be multithreaded using 11 threads. Once the correct password was found, the program would modify a global variable, add the password to it, and then end the loop. The password was linkinpark and the username was v0idcache. After logging into the server I changed to the home directory and found the file flag.txt. I used 'cat flag.txt' and got this flag CMSC389R-{brut3_f0rce_m4ster}.
*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*
