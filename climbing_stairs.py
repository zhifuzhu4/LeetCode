"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

Note:
其实是Fibonacci Number. e.g. n = 100, 假设登到99台阶有m种方法，登到98台阶有n种方法，那么从99到100都是上一步，所以还是m种方法.
从98台阶登到100都是一次登两个台阶，还是n种方法，若果在98登一个台阶，就是到了99, 这种方法已经包含在最初登到99台阶的m种方法中了。
所以登到100的方法就是m+n.

Variable a tells you the number of ways to reach the current step,
and b tells you the number of ways to reach the next step.
So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b,
since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(2, n+1):
            a, b, = b, a + b
        return b

    def climbStairs2(self, n: int) -> int:
        res = [1] * (n+1)
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
