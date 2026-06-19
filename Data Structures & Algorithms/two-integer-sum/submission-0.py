class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for i, j in enumerate(nums):
            if target-j in records:
                return [records[target-j],i]
            records[j] = i
        return []