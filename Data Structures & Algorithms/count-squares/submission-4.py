class CountSquares:
    def __init__(self):
        self.ptsCounts=defaultdict(int)
        self.pts=[]
    def add(self, point: List[int]) -> None:
        self.ptsCounts[tuple(point)]+=1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res=0
        px, py=point
        for x, y in self.pts:
            if (abs(py-y)!=abs(px-x)) or x ==px or y==py:
                continue
            res+=self.ptsCounts[(x, py)] * self.ptsCounts[(px, y)] 
        return res
            
        
        