class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r: int, c: int, n: int) -> 'Node':
            first = grid[r][c]
            same = True

            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(first == 1, True, None, None, None, None)

            half = n // 2
            return Node(
                True, False,
                dfs(r, c, half),
                dfs(r, c + half, half),
                dfs(r + half, c, half),
                dfs(r + half, c + half, half)
            )

        return dfs(0, 0, len(grid))