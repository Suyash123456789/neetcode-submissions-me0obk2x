from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts=[]

    def add(self, point):
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point):
        res = 0
        px, py = point

        for x, y in self.pts:
            # must be a diagonal of an axis-aligned square
            if abs(px - x) != abs(py - y) or (px == x and py == y):
                continue

            res += (
                self.ptsCount[(x, py)]
                * self.ptsCount[(px, y)]
            )

        return res