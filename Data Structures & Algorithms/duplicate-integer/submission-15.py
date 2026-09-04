class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isThere = set()

        for n in nums:
            if n in isThere:
                return True
            isThere.add(n)
        return False