class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]  # Start with the first element
        max_sum = nums[0]  # Start with the first element as the initial max
        
        for num in nums[1:]:
            # If adding num to current_sum makes it smaller than num itself,
            # start a new subarray from num.
            current_sum = max(current_sum + num, num)
            
            # Update max_sum if current_sum is larger
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum