class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #     [1,2,4,6]
        #  -> [1,1,2,8]
        #  <- [48,24,6,1]
        # out:[48,24,12,8]

        # [0, -1, 0, 0, 6]
        # [0, 6, 6, 3, 0]

        out = [0] * len(nums)
        out[0] = 1

        for i in range(1, len(nums), 1):
            out[i] = out[i - 1] * nums[i - 1]

        roll = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * roll
            roll *= nums[i]

        return out
