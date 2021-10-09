# Lab2 CTF Writeup

11911409	孙永康

### Question 1 ：

I first check out the c code, and I found a buffer which is initial at 16 chars :

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_15-14-20.png)

Then I found a function, which can detect the fault and then handle me the flag :

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_15-22-22.png)

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_15-22-11.png)

So I tried to overflow that buffer with some input strings bigger than 16 chars :

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_15-15-28.png)

Finally, I got that flag , which is shown in the picture.

### Question 2 ：

I check the c code first, and found a function which is not used called **win**. In which, we can see that if we could execute this function, we can straightly get the flag. Execute it through overflowing the buffer in function **vuln**:

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_20-58-14.png)

So, the problem is how to find two things :

1)	the length of the cache in **vuln**.

2)	the address of the function **win**

After asking for some help to my classmates, they recommend me a tool called **Binary Ninja**, which could turn the execution file into assembly code.

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_21-15-01.png)

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_21-15-29.png)

As we can see in the picture, the length of cache is 0x70, and the return address is 080485cb.

So, we have to insert a string that can make the return address change to the function win 's starting address, and also have to make the arguments of function win right, like "deadbeef"  and " deadc0de".

Life is short, I use python:

![](C:\Users\jerichosun\Desktop\2\Snipaste_2021-09-20_21-50-08.png)

After inserting the string inside. We receive our flag which is shown in the picture.