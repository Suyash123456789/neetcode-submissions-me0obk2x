class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        res=[]

        for n in nums:
            count[n]=1+count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1, -1, -1):
            for c in freq[i]:
                if len(res)==k:
                    break
                res.append(c)
                
        return res