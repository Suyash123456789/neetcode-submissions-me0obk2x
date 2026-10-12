class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        copy = set()
        res = []

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in copy:
                    cur.append(nums[i])
                    copy.add(nums[i])
                    dfs(cur)
                    copy.remove(nums[i])
                    cur.pop()
        dfs([])
        return res