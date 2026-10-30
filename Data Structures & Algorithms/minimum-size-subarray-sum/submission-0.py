class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_sub = -1
        l, r = 0, 0
        rolling_sum = 0
        while l < len(nums):
            rolling_sum += nums[l]
            l += 1
                # compare with “subarray”, replace if needed
            while rolling_sum >= target:
                    length = l - r
                    if len_sub == -1:
                        len_sub = length
                    elif len_sub > length:
                        len_sub = length
                    prev_digit = nums[r]
                    r += 1
                    rolling_sum -= prev_digit
        if len_sub == -1: return 0
        return len_sub
