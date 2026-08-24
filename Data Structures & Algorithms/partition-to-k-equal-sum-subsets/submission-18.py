class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        used = [False] * len(nums)
        nums.sort(reverse = True)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if not used[j] and subsetSum + nums[j] <= target:
                    used[j] = True
                    subsetSum += nums[j]
                    if backtrack(j + 1, k, subsetSum):
                        return True
                    subsetSum -= nums[j]
                    used[j] = False
            return False

            
        return backtrack(0, k, 0)
