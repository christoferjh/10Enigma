# 10Enigma
Binary enigma https://makerworld.com/en/models/247798#profileId-264026

# Usage:
The converter will replace all your spaces to "_" and it will also make your string uppercase.
If you see a "Ö" in the output, something have gone wrong and check your input.

## Convert to binary
```python Enigma.py -B [text to convert to binary]```
## Convert to text
```python Enigma.py -A [binary to convert to text]```
## Show convertion table
```python Enigma.py -T```

## Examples
```
$ python Enigma.py -B hello world how are you?
01000 00101 01100 01100 01111 00000 10111 01111 10010 01100 00100 00000 01000 01111 10111 00000 00001 10010 00101 00000 11001 01111 10101 11100
```
```
$ python Enigma.py -A 01000 00101 01100 01100 01111 00000 10111 01111 10010 01100 00100 00000 01000 01111 10111 00000 00001 10010 00101 00000 11001 01111 10101 11100
HELLO_WORLD_HOW_ARE_YOU?
```
```
$ python Enigma.py -T
Letter  Dec     Binary
-------------------------------
_       0       00000
A       1       00001
B       2       00010
C       3       00011
D       4       00100
E       5       00101
F       6       00110
G       7       00111
H       8       01000
I       9       01001
J       10      01010
K       11      01011
L       12      01100
M       13      01101
N       14      01110
O       15      01111
P       16      10000
Q       17      10001
R       18      10010
S       19      10011
T       20      10100
U       21      10101
V       22      10110
W       23      10111
X       24      11000
Y       25      11001
Z       26      11010
.       27      11011
?       28      11100
!       29      11101
0       30      11110
1       31      11111
```
