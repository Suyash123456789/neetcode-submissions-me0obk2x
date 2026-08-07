class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for r in ransomNote:
            if r in count:
                count[r] -= 1
                if count[r] == 0:
                    count.pop(r)
            else:
                return False
        return True