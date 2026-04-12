class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxheight=heights[len(heights)-1]
        res=[len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            if heights[i]>maxheight:
                res.append(i)
                maxheight=heights[i]
            else:
                continue
        res.reverse()
        return res