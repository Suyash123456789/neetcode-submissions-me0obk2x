class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):      
            res = []
            for i in range(4):
               res.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:])
               res.append(lock[:i] + str((int(lock[i]) + 9) % 10) + lock[i + 1:])
            return res

        q = deque()
        q.append(["0000", 0])
        visit = set(deadends)
        while q:  
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child in visit:
                    continue
                q.append([child, turns + 1])
                visit.add((child))
        return -1
