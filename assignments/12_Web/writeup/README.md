# Crypto II Writeup

Name: Ashan Panduwawala
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Ashan Panduwawala

Part 1

The first thing I did was go to the website to find hints on what where to sql inject code. After clicking on each of the href links to each hack, I noticed that a get request was being called as there was a ‘?’ followed by the id that the database was looking for. Using this, I knew that a database was performing a query using the following command: “ SELECT * from tables WHERE id = Variable;.” And so, I tried closing off the initial quote and putting “ 1‘ OR 1=1; “ (without the double quotes) however, the server immediately rejected it, saying that an sql injection was detected. The reason my input was blocked was due to a WAF that noticed the SQL injection.  After this I looked to the slides for help and saw this line: ‘|| 0x50 is not null. This meant that I could bypass the  or restriction without having to use OR. I tried many things such as 1’ || ‘1’=’1’ and 3 || 0<1 however it didn’t work. After some research, I found that I didn’t need the last apostrophe in the statement above (1’ || ‘1’=’1’ ). Then, I tried 1' || '1' = '1 as the url and it gave me all of the hacks in one page and at the bottom was the flag: CMSC389R-{y0u_ar3_th3_SQ1_ninj@}. 


Part 2

Lvl 1: For this problem, I initially just put a random word such as “lol” into the search box. I immediately noticed that it repeated what I said in the result “Sorry, no results were found for lol.” I used inspect element and saw that this was displayed using html so, I entered a script tag and called alert inside it (<script>alert("oof")</script>), giving me the desired alert message.

Lvl 2: This one was much tricker to solve because I tried using the script tag again to solve it. First, I used inspect element to find how the message was being printed. It was inside a blockquote so I tried cancelling out the block quote by typing </blockquote> and then called a script tag to alert however, the script would never run. I couldn’t figure out how to get it to run so I used all three hints because the first two were not helpful, except the last one. Using the onerror attribute, I realized that I could somehow throw an error every time the page was loaded causing some function to run and this could be done using the image tag. The image tag takes a src and if the path is invalid, it throws an error. Using this I called 
<img src=”lmao” onerror='alert()' /> and it worked.

Lvl 3: Given the fact that the buttons are invoking a function in javascript under the hood, I looked at the source code and saw the function choose tab. This function passes in the value from the url without any filtering and adds it to the html. Using this, we can inject code. First, I saw that I needed to close off the quotes in the <img src= ‘  tag. Then, if I simply close this off early, the “.jpg” will not be appended and the file will always throw an error. So, I simply added ' onerror="alert('done');" and it worked.

Lvl 4: Using the same principles as the last level, I looked at the source code and saw that  the starTimer() function is using the passed in values without checking the input. I did use a hint and saw that after I added a  ‘ , an error was thrown in console at a specific line. I then tried to terminate the quote early so that I could inject an alert statement right after in the onload function. Then I closed the function call off with a ‘);‘ and called alert(‘xss, giving me the alert once clicked. ');alert('xss.

Lvl 5: After pressing the button to sign up, the url changed to signup?next=confirm. I looked at the source code and saw that there is a get request on whatever the next field holds ( {'next': self.request.get('next', 'welcome')})). I took this and realized that I could replace the next with any code so I added javascript:alert("XSS") in place of the next field and entered a random email.

Lvl 6: This one was the most confusing out of all of them. Initially, I started playing around with the directories in the url to see what would change on the page. After removing both of the directories after #, I found that it was not being displayed on the page anymore. So I thought I could simply add a quote to end the quote early, create a script using a script tag, and it would be fine however, the website changed all occurrences of “<” and “>” to a random encoded text. After some trouble figuring it out, I stumbled upon the last hint which said to use an online api. I searched it up and found a library that I could add to the url. https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert.




