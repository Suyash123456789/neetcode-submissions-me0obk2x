class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freq, even_freq = 0, len(s)
        for v in freq.values():
            if v % 2:
                odd_freq = max(odd_freq, v)
            else:
                even_freq = min(even_freq, v)
        return odd_freq - even_freq