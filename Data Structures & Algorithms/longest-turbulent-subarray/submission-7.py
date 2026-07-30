class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, (r - l + 1))
                prev = ">"
                r += 1
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, (r - l + 1))
                prev = "<"
                r += 1

            else:
                if arr[r - 1] == arr[r]:
                    l = r
                    r = r + 1
                    prev = ""
                else:
                    l = r - 1
                    prev = ""
        return res