class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = 0
        for index, number in enumerate(nums):
            if number == 0:
                shift += 1
            else:
                nums[index], nums[index - shift] = nums[index - shift], nums[index]
