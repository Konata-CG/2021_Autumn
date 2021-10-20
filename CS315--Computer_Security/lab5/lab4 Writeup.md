# lab4	Writeup

孙永康	11911409



## Part 1

### 1. Read the lab instructions above and finish all the tasks.

First, use **ifconfig** instruction to find ip address of the target machine.

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\登陆并ifconfig.png)

Then, use nmap to scan and find the open port of the the target machine.

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\nmap.png)



### 2. Use nmap to scan the target and find the software version of the OS and the  running services (list at least 3 of the running services). What are the differences  if we use T1, T2, T3 flags? How to avoid detection from an intrusion detection  system (e.g., stealthy scanning)?

Use **nmap -O [ip address]** to scan the OS version and  otherr information of the target machine.

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\OS版本.png)

Then I found the OS version is **Linux 2.6.9 - 2.6.33**.

There are many running servcices, like "**ftp**", "**ssh**", "**mysql**", "**postgresql**".

The diferent between **T1**, **T2**, **T3** is that :

​	**T1** : A little bit faster than **T0**, also can bypass the firewall and IDS.

​	**T2** : A "polite" scanning choice, takes up few bandwidth and resources of the target machine.

​	**T3** : A normal choice of scanning, normal speed, normal resources consumptions, also the default choice.

We can use **T0**/**T1** to bypass the IDS.

By the way, there are few ways to avoid other scan our server :

There is a service in Linux called **Iptables**, which is a important part of the Linux Firewall. The main function of Iptables is to control network data packets to and from the device and forward them. Iptables is used to control data packets that need to enter, exit, forward, and route the device. Use this filtration, nmap cannot scan our device.

	1.	**#iptables -F **
 	2.	**\#iptables -A INPUT -p tcp –tcp-flags ALL FIN,URG,PSH -j Drop **
 	3.	**\#iptables -A INPUT -p tcp –tcp-flags SYN,RST SYN,RST -j Drop **
 	4.	**\#iptables -A INPUT -p tcp –tcp-flags SYN,FIN SYN,FIN -j Drop **
 	5.	**\#iptables -A INPUT -p tcp –tcp-flags SyN SYN –dport 80 -j Drop**



## Part 2

### 1. Read the lab instructions above and finish all the tasks.

First,  follow the instruction, open the service **metasploit**

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\开启metasploit.png)

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\进入metaspolit.png)

Then, open **msfconsole** and then try first exploit:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\attack1.png)

Try second exploit:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\attack2.png)

Use GUI version, add host, scan, and search attack:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\open GUI.png)

Then use ftp backdoor to exploit it:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\ftp.png)

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\ftp_ans.png)



### 2. Why do we need to assign an internal IP address (i.e., behind NAT) for  Metasploitable2-Linux? What will happen if we assign a public IP to it?

Because a public IP is very easily getting attack, and our demo virtual machine is too weak to defend them, put it on internal IP address is much safer and easy for us to lauch attack.



###  3. Besides the two vulnerabilities we used, exploit another vulnerability using both  msfconsole and Armitage. Show me that you have placed a file in the exploited  remote machine via screenshots and by creating the file with the command  “touch ” where  should be replaced with your full name.

We first choose an attack on the internet:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\anotherattacj_0.png)

Launch it to our target machine, and then gain a reverse shell:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\anotherattack.png)

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\anotherattack_2.png)

use **touch <filename>** to create a file using my name, sunyongkang.

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\anotherattack_3.png)

Then, change tp **msfconsole**, do the same thing:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\ANOTHER EXPLOIT.png)