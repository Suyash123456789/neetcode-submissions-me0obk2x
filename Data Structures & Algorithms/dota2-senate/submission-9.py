class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            if c == "D":
                D.append(i)

        while D and R:
            d, r = D.popleft(), R.popleft()
            if d < r:
                D.append(d + len(senate))
            else:
                R.append(r + len(senate))
        if D:
            return "Dire"
        elif R:
            return "Radiant"


        