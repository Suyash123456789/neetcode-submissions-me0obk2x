class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isin= set()

        for i in nums:
            if i in isin:
                return True
            isin.add(i)
        return False

        