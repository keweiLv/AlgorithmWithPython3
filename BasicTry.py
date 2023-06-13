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