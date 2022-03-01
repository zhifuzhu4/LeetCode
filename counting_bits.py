"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 10**5

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n).
Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

Solution 2 notes:
To understand the solution, we remember the following two points from math:
1. All whole numbers can be represented by 2N (even) and 2N+1 (odd).
2. For a given binary number, multiplying by 2 is the same as adding a zero at the end
(just as we just add a zero when multiplying by ten in base 10).
Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's.
Likewise, doubling a number and adding one will increase the count by exactly 1. Or:
countBits(N) = countBits(2N)
countBits(N)+1 = countBits(2N+1)
Thus we can see that any number will have the same bit count as half that number,
with an extra one if it's an odd number.
We iterate through the range of numbers and calculate each bit count successively in this manner:

for i in range(num):
    counter[i] = counter[i // 2] + i % 2

With a few modifications:
Define the base case of counter[0] = 0, and start at 1.
We need to include num, so use num+1 as the bound on the range.
Bit-shifting 1 has the same effect as dividing by 2, and is faster, so replace i // 2 with i >> 1.
We can choose to either initiate our list with counter = [0] * (num+1) or just counter = [0]
and then append to it (which has O(1)). It's a little faster to initiate it with zeroes and
then access it rather than appending each time, but I've chosen the latter for better readibility.
Some solutions use i & 1 to determine the parity of i. While this accomplishes the same purpose as i % 2
and keeps with the bitwise-operator theme, it is faster to calculate the modulus.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = bin(i).count('1')
        return res

    def countBits2(self, n: int) -> List[int]:
        cnt = [0] * (n+1)
        for i in range(1, n+1):
            cnt[i] = cnt[i // 2] + i % 2
        return cnt

    def countBits3(self, n: int) -> List[int]:
        # same as solution 2 but using bit operatoin
        cnt = [0] * (n+1)
        for i in range(1, n+1):
            cnt[i] = cnt[i >> 1] + (i & 1)
        return cnt
