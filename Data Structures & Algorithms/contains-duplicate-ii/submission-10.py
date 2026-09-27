class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        isThere = set()
        l = 0
        for r in range(len(nums)):
            if r > k:
                isThere.remove(nums[l])
                l += 1
            if nums[r] in isThere:
                return True
            isThere.add(nums[r])
        return False