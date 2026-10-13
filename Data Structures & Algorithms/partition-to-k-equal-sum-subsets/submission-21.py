class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        length = total // k
        nums.sort(reverse=True)

        if nums[0] > length:
            return False

        visit = set()

        def dfs(pocket, k):
            if k == 1:
                return True

            if pocket == length:
                return dfs(0, k - 1)

            prev = -1

            for i in range(len(nums)):
                if i in visit:
                    continue

                if nums[i] == prev:
                    continue

                if pocket + nums[i] <= length:
                    visit.add(i)

                    if dfs(pocket + nums[i], k):
                        return True

                    visit.remove(i)
                    prev = nums[i]

            return False

        return dfs(0, k)