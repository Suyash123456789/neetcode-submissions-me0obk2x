class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = Counter(nums) 
        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n]:
                    perm.append(n)
                    count[n] -= 1
                    backtrack()
                    count[n] += 1
                    perm.pop()
        backtrack()
        return res
