
from typing import List


def low_bound(nums: List[int], targe: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < targe:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:

    # 在排序数组中查找元素的第一个和最后一个位置
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = low_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = low_bound(nums, target + 1) - 1
        return [start, end]

    # 和大于等于target的最短子数组
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = left = 0
        for right,v in enumerate(nums):
            s += v
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans != n + 1 else 0

    # 买卖股票的最佳时机
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice,price)
            maxprofit = max(maxprofit,price - minprice)
        return maxprofit