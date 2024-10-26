class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Return x if it's 0 or 1

        left, right = 1, x // 2  # We only need to search up to x // 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid  # Found the exact square root
            elif mid * mid < x:
                left = mid + 1  # Move right to get a larger square
            else:
                right = mid - 1  # Move left to get a smaller square

        # When the loop ends, right is the integer part of the square root of x
        return right