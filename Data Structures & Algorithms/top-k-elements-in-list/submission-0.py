class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tem = Counter(nums)
        
        arr = []
        for i,j in tem.most_common(k):
            arr.append(i)
        return arr