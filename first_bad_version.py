"""
278. First Bad Version

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 2**31 - 1

Note:
Read this tutorial again and again
[Python] Powerful Ultimate Binary Search Template. Solved many problems

Minimize k , s.t. condition(k) is True
The following code is the most generalized binary search template:

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

What's really nice of this template is that, for most of the binary search problems,
we only need to modify three parts after copy-pasting this template,
and never need to worry about corner cases and bugs in code any more:
1. Correctly initialize the boundary variables left and right to specify search space.
    Only one rule: set up the boundary to include all possible elements;
2. Decide return value. Is it return left or return left - 1?
    Remember this: after exiting the while loop, left is the minimal k satisfying the condition function;
3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
