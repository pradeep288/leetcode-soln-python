class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestion = []

    def add_suggestion(self, product):
        if len(self.suggestion) < 3:
            self.suggestion.append(product)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        products = sorted(products)

        for product in products:
            node = root
            for c in product:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.add_suggestion(product)
        result = []

        node = root

        for c in searchWord:
            node=node.children[c]
            result.append(node.suggestion)

        return result
