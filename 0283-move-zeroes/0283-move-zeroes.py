class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroIndex], nums[i] = nums[i], nums[nonZeroIndex]
                nonZeroIndex += 1
        