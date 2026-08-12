class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        isNot = set(i for i in range(1, len(nums) + 1))
        isDouble = None
        for n in nums:
            if n not in isNot:
                isDouble = n
                continue
            isNot.remove(n)
        isNull = next(iter(isNot)) if isNot else len(nums)
        return [isDouble, isNull]
