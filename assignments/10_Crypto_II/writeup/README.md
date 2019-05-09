# Crypto II Writeup

Name: Ashan Panduwawala
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Ashan Panduwawala

## Assignment Writeup

### Part 1 (70 Pts)
<<<<<<< HEAD
The flag is CMSC389R-{m3ss@g3_!n+A_b0ttl3}. I found this by calling gpg --import b_secret.key and then calling gpg --decrypt message.txt.gpg. This gave me a set of instructions to complete along with the flag above.
=======
The flag is CMSC389R-{m3ss@g3_!n+A_b0ttl3}. Using the fact that I was given the key and the file, I knew that all I needed to do was decrypt the file using the key as the password for it. I found this by calling gpg --import b_secret.key and then calling gpg --decrypt message.txt.gpg. This gave me a set of instructions to complete along with the flag above. Next, I called gpg --list-secret-keys and took a screenshot. Then I used vim to open a new file, entered the correct contents, and used cat to make sure it was correct. Next, I called gpg --output signature.txt.asc --clearsign signature.txt to sign the sign it and armor it with ascii. Finally, I checked my output and got the output below.
>>>>>>> a11d0e0674f8238b9e9b0d134f5123f1ce9725b2
### Part 2 (30 Pts)
1. The ecb.bmp file looks substantially different from the original photo however, you can still see the shapes and outlines that were contained in the photo. You can see the oval and the rectancle in the encrypted image which implies that is isn't difficult to make out what the original image was. 
On the other hand, the cbc.bmp file leaves you completely in the dark as to what the original photo was. There are no clues, outlines, or shapes that give us information on the original photo. Simply said, the photo just looks like a bunch of random pixels on a screen.

2. ECB is less secure. The reason for this is that ECB is essentially a raw cipher. It takes a block, encrypts it, and returns it. However, the problem with this is that properties of the plaintext may show up in the ciphertext, Because it encrypts a block at a time and is independent of the other blocks, it usually creates patterns because you are only dealing with the part that you encrypted.

CBC is more secure because each block is dependent on the block before it. Given an initialization vector, you XOR the first block of plaintext with it. Then you encrypt it. The next block however, is xor'd against the last encrypted block before encrypting the current block to almost elminiate any possible patterns.  
