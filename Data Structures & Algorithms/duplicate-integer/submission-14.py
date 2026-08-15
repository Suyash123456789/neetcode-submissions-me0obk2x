class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = set()

        for n in nums:
            if n in hasDuplicate:
                return True
            hasDuplicate.add(n)
        return False
        