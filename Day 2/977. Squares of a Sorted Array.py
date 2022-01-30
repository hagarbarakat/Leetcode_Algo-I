class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
            square *= square
            output[i] = square
        return output
