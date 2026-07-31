class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            while i < len(digits) and one:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
                i += 1
            if one:
                digits.append(1)
                one = 0
        return digits[::-1]
            