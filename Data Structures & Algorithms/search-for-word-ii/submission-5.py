class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store full word at end node


class Solution:
    def findWords(self, board, words):
        # Build Trie
        root = TrieNode()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w   # mark end of word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            # Boundary + pruning checks
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] == "#" or board[r][c] not in node.children):
                return

            ch = board[r][c]
            node = node.children[ch]

            # Found a word
            if node.word:
                res.append(node.word)
                node.word = None   # avoid duplicates

            # Mark visited
            board[r][c] = "#"

            # Explore neighbors
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # Backtrack
            board[r][c] = ch

        # Start DFS from each cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res