class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set()
        l = 0
        for r in range(len(nums)):
            while r - l > k:
                hashSet.remove(nums[l])
                l+=1
            if nums[r] in hashSet:
                return True
            hashSet.add(nums[r])
        return False