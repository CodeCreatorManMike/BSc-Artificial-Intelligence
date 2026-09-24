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



-----
# Self Study

## Number Systems Introduction — Decimal, Binary, Octal & Hexadecimal

There are four main number systems we will work with:

| Number System   | Base | Digits Used |
| --------------- | ---: | ----------- |
| **Decimal**     |   10 | `0–9`       |
| **Binary**      |    2 | `0–1`       |
| **Octal**       |    8 | `0–7`       |
| **Hexadecimal** |   16 | `0–9, A–F`  |

---

## Decimal

**Decimal is Base 10.**

It is the number system we use for everyday counting.

```text
0 1 2 3 4 5 6 7 8 9
```

Example:

```text
348
```

---

## Binary

**Binary is Base 2.**

Binary is heavily used in computing because it only contains two possible digits:

```text
0 1
```

Example:

```text
101011100
```

---

## Octal

**Octal is Base 8.**

It uses the digits:

```text
0 1 2 3 4 5 6 7
```

There is no `8` or `9` in octal.

Example:

```text
534
```

---

## Hexadecimal

**Hexadecimal is Base 16.**

It uses:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

The letters represent decimal values:

| Hex | Decimal |
| --- | ------: |
| A   |      10 |
| B   |      11 |
| C   |      12 |
| D   |      13 |
| E   |      14 |
| F   |      15 |

So:

```text
0123456789ABCDEF
```

---

# Converting Decimal to Binary / Octal / Hexadecimal

To convert a decimal number into another number system, we can use a technique called **successive division**.

The basic idea is:

1. Divide the decimal number by the **base** you want.
2. Record the **remainder**.
3. Divide the quotient again.
4. Keep going until the quotient becomes `0`.
5. Read the remainders **from bottom to top**.

```text
↑
Read
remainders
upwards
↑
```

The number you divide by depends on the destination:

| Conversion            | Divide By |
| --------------------- | --------: |
| Decimal → Binary      |         2 |
| Decimal → Octal       |         8 |
| Decimal → Hexadecimal |        16 |

---

# Decimal → Binary

## Example: Convert `348` to Binary

Because binary is **Base 2**, repeatedly divide by `2`.

```text
348 / 2 = 174 | R0
174 / 2 = 87  | R0
87  / 2 = 43  | R1
43  / 2 = 21  | R1
21  / 2 = 10  | R1
10  / 2 = 5   | R0
5   / 2 = 2   | R1
2   / 2 = 1   | R0
1   / 2 = 0   | R1
```

Now read the remainders **from bottom to top**:

```text
101011100
```

Therefore:

```text
348₁₀ = 101011100₂
```

or simply:

```text
348 = 101011100
```

---

# Decimal → Octal

## Example: Convert `348` to Octal

Because octal is **Base 8**, repeatedly divide by `8`.

```text
348 / 8 = 43 | R4
43  / 8 = 5  | R3
5   / 8 = 0  | R5
```

Read the remainders **from bottom to top**:

```text
534
```

Therefore:

```text
348₁₀ = 534₈
```

or:

```text
348 = 534
```

---

# Decimal → Hexadecimal

## Example: Convert `348` to Hexadecimal

Because hexadecimal is **Base 16**, repeatedly divide by `16`.

```text
348 / 16 = 21 | R12
21  / 16 = 1  | R5
1   / 16 = 0  | R1
```

Remember:

```text
12 = C
```

So the remainders are:

```text
C
5
1
```

Read them **from bottom to top**:

```text
15C
```

Therefore:

```text
348₁₀ = 15C₁₆
```

or:

```text
348 = 15C
```

---

# Converting Back to Decimal

When converting **to decimal**, we do not use successive division.

Instead, we use **place values / powers of the base**.

The general pattern is:

```text
digit × base^position
```

Positions start at `0` from the **right-hand side**.

Example positions:

```text
4 3 2 1 0
↓ ↓ ↓ ↓ ↓
1 0 1 1 0
```

---

# Binary → Decimal

Binary uses **Base 2**.

For example:

```text
10110101
```

Starting from the right:

```text
1 × 2^0
0 × 2^1
1 × 2^2
0 × 2^3
1 × 2^4
1 × 2^5
0 × 2^6
1 × 2^7
```

So:

```text
(1 × 2^7)
+ (0 × 2^6)
+ (1 × 2^5)
+ (1 × 2^4)
+ (0 × 2^3)
+ (1 × 2^2)
+ (0 × 2^1)
+ (1 × 2^0)
```

Calculate the values:

```text
128 + 0 + 32 + 16 + 0 + 4 + 0 + 1
```

```text
= 181
```

Therefore:

```text
10110101₂ = 181₁₀
```

---

# Octal → Decimal

Octal uses **Base 8**.

Example:

```text
534
```

Positions:

```text
2 1 0
↓ ↓ ↓
5 3 4
```

Calculate:

```text
(5 × 8^2)
+ (3 × 8^1)
+ (4 × 8^0)
```

```text
= (5 × 64)
+ (3 × 8)
+ (4 × 1)
```

```text
= 320 + 24 + 4
```

```text
= 348
```

Therefore:

```text
534₈ = 348₁₀
```

---

# Hexadecimal → Decimal

Hexadecimal uses **Base 16**.

Example:

```text
15C
```

Remember:

```text
C = 12
```

Positions:

```text
2 1 0
↓ ↓ ↓
1 5 C
```

Calculate:

```text
(1 × 16^2)
+ (5 × 16^1)
+ (12 × 16^0)
```

```text
= (1 × 256)
+ (5 × 16)
+ (12 × 1)
```

```text
= 256 + 80 + 12
```

```text
= 348
```

Therefore:

```text
15C₁₆ = 348₁₀
```

---

# Binary → Octal

Binary and octal have a useful shortcut.

Every **3 binary digits** correspond to **1 octal digit**.

Starting from the **right**, split the binary number into groups of 3.

Example:

```text
101011100
```

Split:

```text
101 | 011 | 100
```

Convert each group:

```text
101 = 5
011 = 3
100 = 4
```

Therefore:

```text
101011100₂ = 534₈
```

### Binary → Octal Table

| Binary | Octal |
| ------ | ----: |
| 000    |     0 |
| 001    |     1 |
| 010    |     2 |
| 011    |     3 |
| 100    |     4 |
| 101    |     5 |
| 110    |     6 |
| 111    |     7 |

---

# Octal → Binary

This works in reverse.

Convert every octal digit into **3 binary digits**.

Example:

```text
534
```

Convert each digit:

```text
5 = 101
3 = 011
4 = 100
```

Combine them:

```text
101 011 100
```

Therefore:

```text
534₈ = 101011100₂
```

---

# Binary → Hexadecimal

Every **4 binary digits** correspond to **1 hexadecimal digit**.

Example:

```text
101011100
```

Start grouping from the right:

```text
1 | 0101 | 1100
```

Add leading zeros if necessary:

```text
0001 | 0101 | 1100
```

Convert each group:

```text
0001 = 1
0101 = 5
1100 = 12 = C
```

Therefore:

```text
101011100₂ = 15C₁₆
```

---

# Hexadecimal → Binary

Convert every hexadecimal digit into **4 binary digits**.

Example:

```text
15C
```

Convert:

```text
1 = 0001
5 = 0101
C = 1100
```

Combine:

```text
0001 0101 1100
```

Leading zeros can be removed:

```text
101011100
```

Therefore:

```text
15C₁₆ = 101011100₂
```

---

# Binary ↔ Hexadecimal Table

| Decimal | Binary | Hex |
| ------: | ------ | --- |
|       0 | 0000   | 0   |
|       1 | 0001   | 1   |
|       2 | 0010   | 2   |
|       3 | 0011   | 3   |
|       4 | 0100   | 4   |
|       5 | 0101   | 5   |
|       6 | 0110   | 6   |
|       7 | 0111   | 7   |
|       8 | 1000   | 8   |
|       9 | 1001   | 9   |
|      10 | 1010   | A   |
|      11 | 1011   | B   |
|      12 | 1100   | C   |
|      13 | 1101   | D   |
|      14 | 1110   | E   |
|      15 | 1111   | F   |

---

# Quick Conversion Cheat Sheet

## Decimal → Binary

```text
Divide by 2 repeatedly.
Record each remainder.
Read remainders from BOTTOM → TOP.
```

Example:

```text
348₁₀ → 101011100₂
```

---

## Decimal → Octal

```text
Divide by 8 repeatedly.
Record each remainder.
Read remainders from BOTTOM → TOP.
```

Example:

```text
348₁₀ → 534₈
```

---

## Decimal → Hexadecimal

```text
Divide by 16 repeatedly.
Record each remainder.
Convert 10–15 into A–F.
Read remainders from BOTTOM → TOP.
```

```text
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F
```

Example:

```text
348₁₀ → 15C₁₆
```

---

## Binary → Decimal

```text
Start powers at 0 from the RIGHT.

Multiply each digit by:

2^position

Then add everything together.
```

Example:

```text
10110101₂ → 181₁₀
```

---

## Octal → Decimal

```text
Start powers at 0 from the RIGHT.

Multiply each digit by:

8^position

Then add everything together.
```

Example:

```text
534₈ → 348₁₀
```

---

## Hexadecimal → Decimal

```text
Replace A–F with 10–15.

Start powers at 0 from the RIGHT.

Multiply each digit by:

16^position

Then add everything together.
```

Example:

```text
15C₁₆ → 348₁₀
```

---

## Binary → Octal

```text
Split binary into groups of 3 from the RIGHT.

Convert each group into one octal digit.
```

```text
101 | 011 | 100
 5  |  3  |  4

101011100₂ = 534₈
```

---

## Octal → Binary

```text
Turn every octal digit into 3 binary digits.
```

```text
5   3   4
↓   ↓   ↓
101 011 100

534₈ = 101011100₂
```

---

## Binary → Hexadecimal

```text
Split binary into groups of 4 from the RIGHT.

Convert each group into one hexadecimal digit.
```

```text
0001 | 0101 | 1100
  1  |   5  |   C

101011100₂ = 15C₁₆
```

---

## Hexadecimal → Binary

```text
Turn every hexadecimal digit into 4 binary digits.
```

```text
1    5    C
↓    ↓    ↓
0001 0101 1100

15C₁₆ = 101011100₂
```

---

# The Most Important Rules to Remember

```text
DECIMAL → something
= DIVIDE repeatedly by the destination base
= read remainders BOTTOM → TOP
```

```text
something → DECIMAL
= multiply digits by powers of that number system's base
= positions start at 0 from the RIGHT
= add everything together
```

```text
BINARY ↔ OCTAL
= groups of 3 bits
```

```text
BINARY ↔ HEXADECIMAL
= groups of 4 bits
```

```text
Decimal = Base 10
Binary  = Base 2
Octal   = Base 8
Hex     = Base 16
```

## Easy Memory Trick

```text
TO decimal      → POWERS
FROM decimal    → DIVISION
Binary ↔ Octal  → GROUP 3
Binary ↔ Hex    → GROUP 4
```
