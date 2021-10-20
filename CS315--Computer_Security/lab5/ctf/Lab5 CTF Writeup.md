# Lab5 CTF Writeup

11911409	孙永康



## 1. Jiaran!!!

First I read the target code of this problem and find this function. I found that if we use the right **user name** and **user ID** in **coockie**, we will get the final flag.

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\Snipaste_2021-10-18_15-53-59.png)

So, I choose to use **Burp suite** to check what this requests look like, and then I found this:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\burp.png)

use python to try User id form 100 to 1000:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\Snipaste_2021-10-18_15-57-12.png)

then I found 822 is right

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\822.png)

Here is my flag:

![](E:\GitHub\repositories\2021_Autumn\CS315--Computer_Security\lab5\pic\flag.png)