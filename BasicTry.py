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
