class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Example usage
root = TrieNode()
root.children['a'] = TrieNode()
root.children['a'].is_end_of_word = True
