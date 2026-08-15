class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for i in range(len(strs)):
            key = [0] * 26
            for c in strs[i]:
                key[ord(c) - ord('a')] += 1
            groups[tuple(key)].append(strs[i])
        return list(groups.values())
        