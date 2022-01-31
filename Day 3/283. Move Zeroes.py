class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow, curr = 0, 0
        while curr < len(nums):
            if nums[curr] != 0:
                nums[slow], nums[curr] = nums[curr], nums[slow]
                slow += 1
            curr += 1
