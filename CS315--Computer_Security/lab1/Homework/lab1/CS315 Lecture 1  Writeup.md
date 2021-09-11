# CS315	Lab 1 	Writeup

孙永康	11911409

### 1.Carefully read the lab instructions and finish all tasks above.

yes, I have finish all task in the lab material, but I still have problem about a part of "wireshark" which is named "follow *** stream". I wonder how to read those words and what is the meaning of those information.

### 2.If a packet is highlighted by black, what does it mean for the packet? 

TCP packets with problems

### 3.What is the filter command for listing all outgoing http traffic?

http and ip.src == your network IP

### 4.Why does DNS use Follow UDP Stream while HTTP use Follow TCP Stream?

DNS use UDP protocol which is faster but unstable. HTTP use TCP protocol since 'http' need accurate data transportation but not speed.

### 5.Using Wireshark to capture the FTP password.

choose to right settings: because of the ftp server is at 127.0.0.1, so we choose to catch pack delivered by loopback network card.

![](C:\Users\jerichosun\Desktop\lab1\settings.png)

then we start connecting ftp server with terminal.

![](C:\Users\jerichosun\Desktop\lab1\registerin.png)

that is all pack wireshark caught when I register in FTP server.

![](C:\Users\jerichosun\Desktop\lab1\caughtpack.png)

As we can see, the pack 6 and pack 10 has the information we want.

username:

![](C:\Users\jerichosun\Desktop\lab1\username.jpg)

password:

![](C:\Users\jerichosun\Desktop\lab1\password.jpg)

By the there are other TCP protocol packs along with FTP packs. the first three of those are used to shake hands with the server.

