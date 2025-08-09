class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, current in enumerate(nums):
            difference = target - current
            if difference in ht:
                return i, ht[difference]
            ht[current] = i