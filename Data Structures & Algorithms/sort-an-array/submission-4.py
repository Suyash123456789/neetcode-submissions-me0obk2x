class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            l = r = 0
            k = L

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr[k] = left[l]
                    l += 1
                else:
                    arr[k] = right[r]
                    r += 1
                k += 1

            while l < len(left):
                arr[k] = left[l]
                l += 1
                k += 1

            while r < len(right):
                arr[k] = right[r]
                r += 1
                k += 1

            return arr

        def mergeSort(arr, l, r):
            if l >= r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)