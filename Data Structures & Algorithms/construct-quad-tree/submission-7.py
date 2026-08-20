class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(n, r, c):
            allSame = True

            for i in range(n):
                for j in range(n):
                    if grid[r + i][c + j] != grid[r][c]:
                        allSame = False
                        break
                if not allSame:
                    break

            # Entire region contains the same value
            if allSame:
                return Node(bool(grid[r][c]), True)

            # Divide into 4 quadrants
            n //= 2

            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            return Node(
                True,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return dfs(len(grid), 0, 0)