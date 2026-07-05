class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # Find peak
        l, r = 1, length - 2

        while l <= r:
            mid = (l + r) // 2

            left = mountainArr.get(mid - 1)
            curr = mountainArr.get(mid)
            right = mountainArr.get(mid + 1)

            if left < curr < right:
                l = mid + 1
            elif left > curr > right:
                r = mid - 1
            else:
                peak = mid
                break

        # Binary search left side: increasing
        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # Binary search right side: decreasing
        l, r = peak + 1, length - 1

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m

        return -1