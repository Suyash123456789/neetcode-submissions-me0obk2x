class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm = {}
        res = ''
        for char in s:
            hm[char] = 1+hm.get(char,0)
        
        for char in order:
            if char in hm:
                for i in range(hm[char]):
                    res+=char
                hm.pop(char)
            else:
                continue
        for key, val in hm.items():
            for i in range(val):
                res+=key
        return res