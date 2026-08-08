class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lower_bound(nums, target):
            n = len(nums)
            low, high = 0, n - 1
            lb = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return lb

        def upper_bound(nums, target):
            n = len(nums)
            low, high = 0, n - 1
            ub = n

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ub

        lb = lower_bound(nums, target)

        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub = upper_bound(nums, target)

        return [lb, ub - 1]