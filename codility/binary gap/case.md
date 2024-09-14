Binary Gap Problem
Problem Description
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

Examples:
The number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.


Here's a sample README.md file based on the image you provided, describing the binary gap problem:

Binary Gap Problem
Problem Description
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

Examples:
The number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.
Task:
Write a function:

python
Copy code
def solution(N):
    # Your implementation goes here
The function should return the length of the longest binary gap for a given positive integer N. If N does not contain a binary gap, the function should return 0.

Example Test Cases:
Input: 1041
Binary Representation: 10000010001
Output: 5
Input: 32
Binary Representation: 100000
Output: 0
Constraints:
N is an integer within the range [1..2,147,483,647].
Solution
You need to write an efficient algorithm that converts the integer N into its binary form, detects the binary gaps (sequences of zeros surrounded by ones), and returns the length of the longest gap.

