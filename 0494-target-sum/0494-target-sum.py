class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        
        dp = defaultdict(int)
        dp[0] = 1  # Start with sum 0 having one way
        
        for num in nums:
            next_dp = defaultdict(int)
            for current_sum, count in dp.items():
                next_dp[current_sum + num] += count
                next_dp[current_sum - num] += count
            dp = next_dp  # Move to the next state
        
        return dp[target]