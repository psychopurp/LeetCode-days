#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start


class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     slow,fast=0,0
    #     while slow<len(nums) and fast<len(nums):
    #         if nums[slow]!=0:
    #             slow+=1
    #             continue
    #         if nums[fast]==0:
    #             fast+=1
    #             continue
    #         if slow>fast:
    #             fast+=1
    #             continue
    #         else:
    #             nums[slow]=nums[fast]
    #             nums[fast]=0
    #             fast+=1
    #             slow += 1

    def moveZeroes(self, nums: List[int]) -> None:
        # 添加另一种写法
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != zero:
                    nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1

# @lc code=end
