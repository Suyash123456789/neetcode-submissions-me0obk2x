class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_set=set()
        for n in nums:
            if n in duplicate_set:
                return True
            duplicate_set.add(n)
        return False