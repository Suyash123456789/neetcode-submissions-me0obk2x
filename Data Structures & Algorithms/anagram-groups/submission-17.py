class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for i in range(len(strs)):
            key = [0] * 26
            for c in strs[i]:
                key[ord(c) - ord('a')] += 1
            ana[tuple(key)].append(strs[i])
        return list(ana.values())