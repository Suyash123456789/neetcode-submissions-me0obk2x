class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            co = defaultdict(int)
            if len(count) > 2:
                for na, c in count.items():
                    c = c - 1
                    if c:
                        co[na] = c
                count = co
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
