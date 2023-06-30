from collections import Counter
from typing import List


# 数元素
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for i in arr:
            if i + 1 in arr:
                count += 1
        return count


# 执行操作后的变量值
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if op[1] == '+' else -1 for op in operations)


# 数组中不等三元式的数目
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        ans = a = 0
        for b in cnt.values():
            c = n - a - b
            ans += a * b * c
            a += b
        return ans

    # 打家劫舍
    def rob(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        for i in nums:
            pre, cur = cur, max(cur, pre + i)
        return cur

    # 打家劫舍二
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            pre, cur = 0, 0
            for num in nums:
                pre, cur = cur, max(cur, pre + num)
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]

    # 消除游戏
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left = True
        while n > 1:
            if left or n % 2 != 0:
                head += step
            step <<= 1
            n >>= 1
            left = not left
        return head

    # 回环句
    def isCircularSentence(self, sentence: str) -> bool:
        ss = sentence.split()
        n = len(ss)
        return all(s[-1] == ss[(i+1) % n][0] for i,s in enumerate(ss))
