class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        res = []

        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == "/":
                    if f[:i] in folder_set:
                        res.pop()
                        folder_set.remove(f)
                        break
        return res
        