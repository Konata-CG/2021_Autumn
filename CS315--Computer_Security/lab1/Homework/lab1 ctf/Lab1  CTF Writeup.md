# Lab1 	CTF Writeup

孙永康	11911409

## Question 1 :

This question give me some hint of "UDP" and "streams", so I try to follow those streams in wireshark.

then I find a "not a flag", but I realize that I can change the button of "stream" at the right bottom to quickly check all the other steams with different number.

![](C:\Users\jerichosun\Desktop\lab1 ctf\Snipaste_2021-09-12_02-27-13.png)

and then I find this one when I change the stream number to 6:

![](C:\Users\jerichosun\Desktop\lab1 ctf\Snipaste_2021-09-12_02-16-50.png)

![](C:\Users\jerichosun\Desktop\lab1 ctf\Snipaste_2021-09-12_02-17-09.png)

The flag I found is **picoCTF{StaT31355_636f6e6e}**



## Question 2 :

This problem give us 2 files, first one which can be opened in wireshark  maybe contains the HTTP pack and  we can found flags in it. Second one is a log file which indicates that it is used in SSL/TSL protocols.

![](C:\Users\jerichosun\Desktop\Snipaste_2021-09-12_03-02-50.png)

After searching some information on internet, I notice that SSL/TSL is used by HTTP protocols to encrypt its message. So, searching more information about how to use wireshark to decrypt these kind of decryptions. Then I found this article[[[https\][tls] 如何使用wireshark查看tls/https加密消息--使用keylog - toong - 博客园 (cnblogs.com)](https://www.cnblogs.com/hugetong/p/11437091.html)]. Follow the instructions of the articles, I put log file into the wireshark:

![](C:\Users\jerichosun\Desktop\Snipaste_2021-09-12_02-51-50.png)



The block in the bottom is used to put in blog file. However I can not fully acknowledge what these settings all about, I think I may do some further research later.

However, After putting it in, everything become better. Easily filter with "http contains "flag"" , I found the only one left which absolutely contains the flag.

![](C:\Users\jerichosun\Desktop\Snipaste_2021-09-12_03-00-09.png)

So, the flag is **flag{y2*Lg4cHe@Ps}**