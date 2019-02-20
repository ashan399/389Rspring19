## Assignment Writeup

### Part 1 (45 pts)

1. v0idcache’s real name is Elizabeth Moffet. I found this after searching up her username on inteltechniques and getting a hit on twitter. 
2. She is a banking CEO at 1137bank.money. The details of her work were in her twitter bio. http://1337bank.money/
3. Her email is v0idcache@protonmail.com. I found it on the "about" tab of her website (the website's url was on her twitter). She also has a twitter with the username: v0idcache. Moreover, she uses pastebin under the username v0idcache, and has an acquaintance called F1inch. I found this using inteltechniques.
4. I went on security trails and pasted the domain of the website. The results returned with an ip address of 142.93.136.81. With this ip, I went to iplocation.net and found that the ip was located in Amsterdam City, Netherlands.
5. I added robots.txt to the end of the url and found the directory name: /secret_directory. After adding the directory to the url, I got the tag : CMSC389R-{h1ding_fil3s_in_r0bots_L0L}. After logging into the server I changed to the home directory and found the file flag.txt. I used 'cat flag.txt' and got this flag CMSC389R-{brut3_f0rce_m4ster}. 
6. On kali, I ran nmap on the ip address and scanned all 60000+ ports. I got 3 ports 22, 80, 1337. Port 22 is running on ssh, port 80 is running on http, and port 1337 is running on waste.
7. Taking the ip address that I found, I entered it into mxtoolbox.com and found that the server was running on Werkzeug/0.14.1 Python/3.7.2. 
8. On the bank website, I did inspect element and found the phrase {h1dd3n_1n_plain_5ight}  in the HTML. I also found one using centralops.net and entering the url of her website; Under DNS records, there is a text  field saying "CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}". After logging in and getting access to the shell, I changed to the home/files directory. After typing ls, I saw a ton of files, so I did cat AB4300.txt and found the flag CMSC389R-{YWX4H3d3Bz6dx9lG320dv0JZh}



### Part 2 (75 pts)

For this part, I modified the python stub code to enter all possible passwords into the server. At first I tried different ports running the program to see if anything happened, however, port 1337 was the only one to give a response. Since I had an idea of the username (v0idcache), I was able to try every possible password combination on the server using a txt file called rockyou.txt. After opening the text file, I converted every line in the file into an element of the array x. I then used a counter variable 'c' to iterate 11 elements at a time. The 11 threads must join before moving on to the next set of 11. Everytime I tried a password, I would see if the data returned was a success. However, going through each password one by one was very slow, so I modified the program to be multithreaded using 11 threads. Once the correct password was found, the program would modify a global variable, add the password to it, and then end the loop. The password was linkinpark and the username was v0idcache. Then I nc'd into the website, entered the credentials, and got in. After gaining access to the shell, I changed to the home directory and found a Flag.txt file. After seeing the contents using cat, I got a flag saying CMSC389R-{brut3_f0rce_m4ster}.

The python file is in the same directory as this file

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*


