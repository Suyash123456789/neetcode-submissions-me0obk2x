class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0

        for i, n in enumerate(nums):
            if 1<=abs(n)<=len(nums):
                val=abs(n)-1
                if nums[val]>0:
                    nums[val]*=-1
                else:
                    nums[val]=-1*(len(nums)+1)


        for i, n in enumerate(nums):
            if n>=0:
                return i+1
        return len(nums)+1
                