class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products = sorted(products)
        class Trie():
            def __init__(self, letter= None, children= {}, products = []):
                self.letter = letter
                self.children = children
                self.products = products
        rootNode = Trie()
        for p in products:
            root = rootNode
            for letter in p:
                if letter not in root.children:
                    root.children[letter] = Trie(letter, {}, [])
                root = root.children[letter]
                root.products.append(p)
        retList = []
        root = rootNode
        for letter in searchWord:
            if letter in root.children:
                root = root.children[letter]
                retList.append(root.products[:3])
            else:
                root.children = []
                retList.append([])
        return retList