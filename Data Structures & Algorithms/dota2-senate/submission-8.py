class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            if R[0] < D[0]:
                n = R.popleft()
                D.popleft()
                R.append(n + len(senate))
            else:
                n = D.popleft()
                R.popleft()
                D.append(n + len(senate))
        return "Radiant" if R else "Dire"
