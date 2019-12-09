# Virtual-Machine

### This is Python Virtual Machine.
We are using decryptor.bin file to decode q1_encr.txt file. There are total 717 symbols and letters in q1_encr.txt
16 register commands are used here.

https://www.hexed.it - here you can check binary file.

We are executing instruction by binary file.</br>
Flag register is on of off.</br>
![alt text](https://github.com/CodeForVGTU/Virtual-Machine/blob/master/images/8bits.png)
![alt text](https://github.com/CodeForVGTU/Virtual-Machine/blob/master/images/8bitsXY.png)

Everything in binary file is dividede into pairs:
```
switch:
case: 04 40 --> reg[0]=HEX(40)=int(64)
case: 10 01 --> Ry0000 Rx0001(shiftinimai, kad prirasytume nulius) -->reg[1]=Q=81, does filme came to the end?
0A 1A: is flag on - counter + 1A or false counter + 2?, by this we can go truth every command
10 02 --> reg[2]-->H=72
10 03 --> reg[3]-->A=65
0D 02 --> reg[2]-->reg[2]-reg[0]=72-64=8
0D 03 --> reg[3]-->reg[3]-reg[0]=65-64=1
05 03 --> reg[3]=1 << 1 --> 0000 0001 << 1 0000 0010 = 2
05 03 --> reg[3]=4
05 03 --> 8
05 03 --> 16
0F 32 --> reg[2]=reg[2] OR reg[3] = 8 or 16 = 24
0E 12 --> XOR 1 ir 2, 81 XOR 24 = 73
11 02 --> cout << char(73)=
07 E6 --> counter + E3(-26)
0B 00
```
## COMMAND LIST
![alt text](https://github.com/CodeForVGTU/Virtual-Machine/blob/master/images/1.png)
![alt text](https://github.com/CodeForVGTU/Virtual-Machine/blob/master/images/2.png)
