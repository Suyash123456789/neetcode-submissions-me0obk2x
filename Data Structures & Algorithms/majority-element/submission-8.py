class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if n != res:
                if count == 0:
                    res = n
                else:
                    count -= 1
                    continue 

            count += 1
        return res