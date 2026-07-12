class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,2,8,48] -> [1,1,2,8]
        # [48,48,24,6] <- [48,24,6,1]

        # [0, -1, 0, 0, 6]
        # [0, 6, 6, 3, 0]
        left = len(nums) * [0]
        right = len(nums) * [0]
        left[0] = 1
        right[len(nums) - 1] = 1
        
        for i in range(len(nums) - 1):
            left[i + 1] = nums[i] * left[i]

        for i in range(len(nums) - 1, 0, -1): # from len-1 > 0
            right[i - 1] = nums[i] * right[i]
        print(left)
        print(right)
        out = len(nums) * [0]
        for i in range(len(nums)):
            out[i] = left[i] * right[i]

        return out
