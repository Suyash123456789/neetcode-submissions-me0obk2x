class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()

        for n in nums:
            if hashset and n in hashset:
                return True
            hashset.add(n)
        return False