class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        k=len(nums)-k
        while k:
            heapq.heappop(nums)
            k-=1
        return nums[0]