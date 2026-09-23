# COMP4009: Foundations of Computer Systems (Semester 1 2026-2027:1[OBO])

**Notes:**

## Read before Week 2

- https://research.ebsco.com/plink/016107f9-1bcd-39c4-878a-89bd1a3330e3
- https://r3-vlebooks-com.oxfordbrookes.idm.oclc.org/Reader?ean=9781473787346
- https://r4-vlebooks-com.oxfordbrookes.idm.oclc.org/EpubReader?ean=1780137909292

---

## Contents

1. [Numbering Systems: Why Binary?](#1-numbering-systems-why-binary)
2. [Lesson 1 Notes: Layers of a Computing System](#2-lesson-1-notes-layers-of-a-computing-system)
3. [Binary](#3-binary)
4. [Binary Conversion Method](#4-binary-conversion-method)
5. [Positional Number Formula](#5-positional-number-formula)
6. [Binary and Hexadecimal](#6-binary-and-hexadecimal)
7. [Binary and Octal](#7-binary-and-octal)
8. [Conversion from Decimal to Binary](#8-conversion-from-decimal-to-binary)
9. [Decimal to Octal](#9-decimal-to-octal)

---

## 1. Numbering Systems: Why Binary?

- Computers themselves understand binary at the hardware level.
- **Transistors:** At the hardware level, circuits are primarily built from transistors. Modern systems have billions of them.
- In digital circuits, electrical signals are interpreted as two logical states:
  - **0** = low voltage
  - **1** = high voltage
  - These states have defined voltage ranges.
- The physical world underlying a computer is **analog**.

---

## 2. Lesson 1 Notes: Layers of a Computing System

*In the order covered in the lesson:*

| Layer | Notes |
|---|---|
| **Communications** | Computers are connected to networks to share information and communicate with other computers (networks / internet). |
| **Applications** | Software developed to solve a specific issue or problem. |
| **Operating systems** | Help manage a computer's resources. |
| **Programming** | Software / instructions to manage and process data. |
| **Hardware** | The physical components of a computer system. |
| **Information** | How information is represented on a computer. Information is stored as binary numbers, using memory and on/off-type switches. |

---

## 3. Binary

**Topics:** Counting numbers, converting from binary to other number bases, and performing basic arithmetic operations in binary.

- The binary system is made up of **bits** (`0` or `1`: off or on).
- **8 bits = 1 byte.** A byte can represent **256 distinct values** (`0`–`255` when unsigned).

### Why binary?

- Computers use electronic devices to store and manipulate information.
- Computers interpret on/off information, which is represented using numbers (**binary digits**).
- Binary uses only **two symbols / digits**.
- To convert a binary number to its corresponding decimal form, multiply each digit by its corresponding power of **2**, then add the results.

---

## 4. Binary Conversion Method

- A number system is identified by its **base**.
- Decimal has **10 digits** (`0`–`9`); binary uses **base 2**.
- For each digit, calculate:

  **Digit × base^(digit position)**

- Count digit positions **from right to left**, beginning at **0**.

---

## 5. Positional Number Formula

For any positional number system:

**Digit value = digit × base^position**

Formula:

`dᵢ × bⁱ`

Where:

- `dᵢ` = the digit
- `b` = the number base
- `i` = the position of the digit, counting from `0` on the right

For a whole number:

`N = Σ(dᵢ × bⁱ)`

### Any numbering system

To work out the value, you need to know the **base** and the **position** of each digit.

### Example: `1011` (binary to decimal)

```text
(1 × 2³) + (0 × 2²) + (1 × 2¹) + (1 × 2⁰)

1 × 8 = 8
0 × 4 = 0
1 × 2 = 2
1 × 1 = 1

8 + 0 + 2 + 1 = 11
```

**Result:** `1011₂ = 11₁₀`

### How to convert a decimal number to binary

Use repeated division by **2** and read the remainders **from bottom to top**. See [Conversion from Decimal to Binary](#8-conversion-from-decimal-to-binary) for worked examples.

---

## 6. Binary and Hexadecimal

- **4 bits** can represent **16 distinct values** (`0`–`15`), matching the **16 hexadecimal symbols**.
- Hexadecimal is **base 16**.
- Its symbols are **`0`–`9` and `A`–`F`** (`A = 10` through `F = 15`).
- **1 byte = 2 hexadecimal digits = 2 nibbles.** One nibble (also spelled *nybble*) is **4 bits**.
- Hexadecimal is essentially a shorter, more human-readable representation of binary: grouping **4 bits** into **1 hexadecimal digit** makes long binary values easier to read.

### Example: `3F4` (hexadecimal to decimal)

`F = 15`, so:

```text
(3 × 16²) + (15 × 16¹) + (4 × 16⁰)
```

---

## 7. Binary and Octal

- **3 bits** can represent the **8 different octal symbols**.
- Octal is **base 8**, using digits **`0`–`7`**.
- For example, decimal `8` is octal `10`, and decimal `9` is octal `11`.

**Example octal number:** `3647₈`

---

## 8. Conversion from Decimal to Binary

**Method:** Repeatedly divide by **2** until the quotient is **0**, recording the remainder each time. Pass the quotient to the next stage. Read the remainders **vertically upward (bottom to top)** to get the binary value.

### Example 1: `10` to binary

```text
10 ÷ 2 = 5  remainder 0
 5 ÷ 2 = 2  remainder 1
 2 ÷ 2 = 1  remainder 0
 1 ÷ 2 = 0  remainder 1
                         ↑ Read upward
```

**Result:** `10₁₀ = 1010₂`

### Example 2: `25` to binary

```text
25 ÷ 2 = 12  remainder 1
12 ÷ 2 =  6  remainder 0
 6 ÷ 2 =  3  remainder 0
 3 ÷ 2 =  1  remainder 1
 1 ÷ 2 =  0  remainder 1
                          ↑ Read upward
```

**Result:** `25₁₀ = 11001₂`

### Example 3: `14` to binary

```text
14 ÷ 2 = 7  remainder 0
 7 ÷ 2 = 3  remainder 1
 3 ÷ 2 = 1  remainder 1
 1 ÷ 2 = 0  remainder 1
                         ↑ Read upward
```

**Result:** `14₁₀ = 1110₂`

---

## 9. Decimal to Octal

**Method:** Repeatedly divide by **8** until the quotient is **0**, keeping the remainder at each stage. Pass the quotient to the next stage. Read the remainders **from bottom to top**.

### Example: `25` to octal

```text
25 ÷ 8 = 3  remainder 1
 3 ÷ 8 = 0  remainder 3
                        ↑ Read upward
```

**Result:** `25₁₀ = 31₈`


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








