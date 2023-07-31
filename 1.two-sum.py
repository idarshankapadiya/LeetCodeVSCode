#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for index, num in enumerate(nums):
            if target-num in numsDict:
                return [numsDict[target-num], index]
            else:
                numsDict[num]= index     
# @lc code=end

