from cmath import inf
from typing import List


# 第 350 场周赛
class Solution:

    # 总行驶距离
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            mainTank -= 5
            ans += 50
            if additionalTank:
                additionalTank -= 1
                mainTank += 1
        return ans + mainTank * 10

    # 找出分区值
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = inf
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])
        return ans
