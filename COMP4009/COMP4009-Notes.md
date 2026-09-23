COMP4009: Foundations of Computer Systems (Semester 1 2026-2027:1[OBO])
Notes:

read before week 2:

https://research.ebsco.com/plink/016107f9-1bcd-39c4-878a-89bd1a3330e3

https://r3-vlebooks-com.oxfordbrookes.idm.oclc.org/Reader?ean=9781473787346

https://r4-vlebooks-com.oxfordbrookes.idm.oclc.org/EpubReader?ean=1780137909292



Numbering Systems:

why binary?
-> computers themselves can only understand binary (on a hardware level)
-> transistors; at a hardware level circuits are primarily built from transistors (modern systems have billions of them)
-> in digital circuits, electrical signals are arranged to interpret two logical states (that being 0 (low voltage) and then 1 (being high voltage)) (these have set voltage ranges)
-> the physical world under a computer is analog


Lesson 1 Notes:
(In Order)
layer of coputing system:
communications - computer are connected to networks to share information / communicate with other computers (networks / internet)
applications - software developed to solve a specific issue / problem
operating systems -  helps manage computers resources
programming - software / instructions to manage and process data
hardware - physical components of the computer system
information - how information is represented on a computer (information is stored as binary numbers), computers store information by using memory and on / off type of switches



Binary:
-> count numbers, conversion bfrom binary to other number base, basic arithmetic operations in binary
-> binary system is made up of bits (0/1 : on or off)
-> 8 bits is a byte (can store up to x)

Why Binary?:
-> computers used electronic devices to store / manipulate inforamation
-> computers only understands on / off information and this i stranslated into numbers (binary digits) 
-> only having two symbols / digits to represent binary numbers
-> to translate a binary number into the corresponding decimal form we have to multiply each digit for each corresponding power of 2


Binary Conversion Method:
-> the first term is refered to as a base
-> decimal numbers have 10 different digits 0-9, but since we are dealing with binary numbers we always make use of a base of 2
-> its always, the digit we are dealling with x the base to the power of the position



Positional Number Formula:

For any positional number system:

**Digit value = digit × base^position**

Formula:

`d_i × b^i`

Where:

- d_i = the digit
- b = the number base
- i = the position of the digit, counting from 0 on the right

For a whole number:

`N = Σ(d_i × b^i)`


Any Numbering System:
-> to work out the value you have to know the base and position

Example:

1011

(1 x 2^3) + (0 x 2^2) + (1 x 2^1) + (1 x 2^0)

1 x 8 = 8
0 x 4 = 0
1 x 2 = 2
1 x 1 = 1

8 + 0 + 2 + 1 = 11


How to convert a decimal number to a binary number:


Binary and Hexadecimal:
-> 4 bits can be used to represent 15 different hexadecimal symbols
-> hexadecimal numbers are numbers in base 16
-> 0-9 A-F
-> a byste is equivalent to 2 hexadecimal numbers, or nybbles (1 nybble=4 bits)

-> hexadecimal essentially is a shorter / more human readible version of binary which combine 4 bits together to make it easier to read them

Example

3F4

(3 x 16^2) + (15 x 16^1) + (4 x 16^0)




Binary and Octal:
-> 3 bits can be used to represent the 8 different octal symbols
-> octal numbers are numbers in bas 8 (0-7)
-> eg: 8 = 10 / 9 = 11

3647 Octal 




Conversion From Decimal To Binary:
-> repeat divisuion by 2 until the quotient is 0 and keep remainder. pass the quotient to the next stage until 0

-> 10 to binary:

10/2 = 5 r0
5/2 = 2 r1
2/2 = 1 r0
1/2 = 0 r1

(take the remainder from the last expression vertically upward to find out the binary value)

10 = 1010


-> 25 to binary:

25/2 = 12 r1
12/2 = 6 r0
6/2 = 3 r0
3/2 = 1 r1
1/2 = 0 r1

25 = 11001


-> 14 to binary:

14/2 = 7 r0
7/2 = 3 r1
3/2 = 1 r1
1/2 = 0 r1

14 = 1110




Decimal To Octal:
-> repeat division by 8 until the quotient is 0 and keep remainder. pass the quotient to the next stage until 0

-> 25 to octal:

25/8




Summary:


-----

Self Study:
Number Systems Introduction - Decimal, Binary, Octal & Hexadecimal:

Decimal:
-> base 10, used for everyday counting 

Binary:
-> base 2, used for computing

Octal: 
-> base 8, 0-7

Hexadecimal:
-> base 16, 0-9 A-F
0123456789ABCDEF (A-F corresponds to 10-15)



How we can convert a decimal into a binary/hexadecimal/octal:
-> we make use of a technique called successive division

348 (example) To Binary
348 / 2 = 174    | R0
174 / 2 = 87     | R0
87 / 2 = 43 (.5) | R1 (cause of the 0.5 extra)
43 / 2 = 21 (.5) | R1
21 / 2 = 10 (.5) | R1
10 / 2 = 5       | R0
5 / 2 = 2        | R1
2 / 2 = 1        | R0
1 / 2 = 0.5      | R1

-> we use the remainder, from the bottom to the top /|\ in order to get the binary value

348 = 101011100


348 (example) To Octal
-> to work out the remainder we need take 0.5 (from 43.5) and multiply it out by 8 (base)
348 / 8 = 43,5 | R4
43 / 8 = 5.375 | R3
5 / 8 = 0,625  | R5

-> we use the remainder, from the bottom to the top in order to get the octal value








