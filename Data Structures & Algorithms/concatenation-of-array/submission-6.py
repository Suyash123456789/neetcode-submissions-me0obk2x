class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # res = []
        # for _ in range(2):
        #     for n in nums:
        #         res.append(n)

        # return res

        length=len(nums)
        for i in range(length):
            nums.append(nums[i])
        return nums
