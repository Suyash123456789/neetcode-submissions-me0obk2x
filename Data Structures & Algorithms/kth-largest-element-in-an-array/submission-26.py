class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        while k:
            n = heapq.heappop(nums)
            k -= 1
            if not k:
                return -n
