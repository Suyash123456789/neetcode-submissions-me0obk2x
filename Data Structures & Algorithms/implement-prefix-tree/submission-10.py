class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]]=TrieNode()
            cur=cur.children[word[i]]
        cur.endOfWord=True

    def search(self, word: str) -> bool:
        cur=self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur=cur.children[word[i]]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur=cur.children[prefix[i]]
        return True
        
        