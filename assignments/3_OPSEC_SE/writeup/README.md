# Writeup 3 - Operational Security and Social Engineering

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Ashan Panduwawala

## Assignment Writeup

### Part 1 (40 pts)

  Using the email on her website, I would contact her posing as a bank teller from her bank. Since I don’t know if she has a bank account at her workplace or somewhere else, I decide to not state the name of the bank. In the email I would tell her that her credit card is being used in Germany, and then ask if this activity was hers? If not, then I would provide a phone number to call if she has any questions. Behind the scenes, I am using an email that had bank in the name and I used a prepaid cell-phone so that she would not know my identity. When she calls, I would play a sound-track that had a lot of phones ringing and people talking to make it seem as if I was in an office. This is where the fun begins. I would talk in a saddened voice, saying “Hi, sorry i’m feeling down, my dog got hit by a plane, but how may I help you?” When she tries to sympathize, I would ask if she had any pets and when she says yes, I would ask what her first pet’s name was. After a moment of talking, I would return to the task and ask to confirm her identity by asking a couple of questions: “What is your mother’s maiden name?” and “What city were you born in?” Generally, most banks ask for background questions so that people can change their password or get into their account if they forgot. Generally, people do not remember what questions they chose, so I use this option to my advantage. If for some reason she remembers her security questions, I would reply saying “Ooops sorry i’m looking at wrong Elizabeth” and then continue. Next I would say “what web browser do you use?” Then I would say “ok so go to our website and check your account’s balance and see if the transaction was removed.” She will go and say yes because there is no transaction there. Next, I will prompt her to change her pin and ask what it is. When she says it, I will type very loudly and sigh after a minute and say “ sorry the machine isn’t responding right now -- the internet must be down or something.” I would then tell her to change it online when she can. Finally, I would say, “ thanks for your cooperation, have a nice day!” Since I bought the pre-paid phone with cash, will not be able to track who I am and so, I will have successfully stolen the information without leaving a trace.


### Part 2 (60 pts)

  1337Bank’s web server had many vulnerabilities that led to exploitation by us hackers. One of them was the password. Aside from the fact that you used the same username across multiple websites, your password was weak and predictable. One of the easiest solutions to this is to create a complex password with a combination of numbers, uppercase letters, and lowercase letters. Additionally, use different usernames across different websites to make it harder for hackers to guess what it is. If you have trouble remembering every password or username, I would suggest using google chrome’s password manager. It remembers your usernames and passwords, while making it difficult to steal from an external source. 

  The second problem was that you had an open port that would accept anything that was sent to it. Port 1337 was a port in which hackers could send data and receive it back without any consequence. One solution is to close all open ports. Doing this would prevent hackers from abusing a port with malicious content. Another solution is to use a web application firewall. A WAF is a firewall for HTTP applications. It monitors data transfer between the server and device and protects against SQL injections and cross-site scripting (1). Another security tip is to switch the website to HTTPS. HTTPS guarantees that people are communicating with only the server they are using (2). This prevents hackers from intercepting or taking over important data by imitating another person. It would also be beneficial to invest in a strong DNS Firewall. A firewall protects users from connecting to known malicious Internet locations, gives insights on threats, and isolates infected devices (4). Another potential investment could be an IDS and an IPS. IDS stands for intrusion detection system and IPS is intrusion prevention system. Both monitor traffic and inspect packets for suspicious data however, an IDS  warns of attacks while an IPS blocks them (3).
  The third problem was that having an open port allowed for unlimited password attempts. This is the main reason why hackers can get into the website in a short period of time. With unlimited attempts, the hacker can abuse the system and try millions of passwords without any resistance. One simple solution is to allow a certain amount of password attempts and if those attempts are used up, a timeout will occur where you will have to wait until you can enter it again. This method binds to the username and the timeouts will continuously increase with the number of attempts. Furthermore, if a certain number of passwords are incorrect, the website can block the username. There are numerous free softwares that test SQL injection, XSS, and many known vulnerabilities such as Netsparker, OpenVAS, and Nessus (2). Additionally it is wise to keep the website’s software updated. For example, if your webpage was using a really old version of some software, hackers will know most of the tricks and holes to it if it is still used.


(1) www.owasp.org
(2) https://www.creativebloq.com/web-design/website-security-tips-protect-your-site-7122853
(3) https://www.pandasecurity.com/usa/support/card?id=31463
(4) https://www.infoblox.com/glossary/dns-firewall/


