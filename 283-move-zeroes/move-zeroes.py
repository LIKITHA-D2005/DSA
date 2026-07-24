class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes = []
        for num in nums:
            if num == 0:
                zeroes.append(num)
        nums[:] = [num for num in nums if num != 0]
        nums.extend(zeroes)