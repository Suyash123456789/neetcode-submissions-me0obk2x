class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(fruits)):
            basket[fruits[r]] = r
            while len(basket) > 2:
                if l == basket[fruits[l]]:
                    basket.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res 