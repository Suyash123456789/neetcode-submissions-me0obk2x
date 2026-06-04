class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        D, R=deque(), deque()

        for i, c in enumerate(senate):
            if c=="R":
                R.append(i)
            else:
                D.append(i)

        i,j=0,0

        while D and R:
            d=D.popleft()
            r=R.popleft()
            if d<r:
                D.append(d+len(senate))
            else:
                R.append(r+len(senate))
        return "Radiant" if R else "Dire"
