class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for c, f in count.items():
            freq[f].append(c)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    break
            if len(res) == k:
                break
        return res
            