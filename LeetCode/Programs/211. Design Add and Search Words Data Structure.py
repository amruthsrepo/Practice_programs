class Trie():
    def __init__(self):
        self.children = {}
        self.isEnd = False
            
class WordDictionary(object):

    def __init__(self):
        self.rootNode = Trie()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        root = self.rootNode
        for letter in word:
            if letter not in root.children:
                root.children[letter] = Trie()
            root = root.children[letter]
        root.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def searchUtil(j, root):
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in root.children.values():
                        if searchUtil(i+1, child):
                            return True
                    return False
                elif c not in root.children:
                    return False
                root = root.children[c]
            return root.isEnd
        return searchUtil(0, self.rootNode)