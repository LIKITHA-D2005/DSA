class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n+1):
            return (n *(n+1))//2 - sum(nums)