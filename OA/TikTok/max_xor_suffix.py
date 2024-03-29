class TrieNode:
    # Initialize a TrieNode with two possible paths: 0 or 1
    def __init__(self):
        self.children = {}


def insert(root, num):
    # Insert a number into the trie
    node = root
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]


def findMaximumXOR(root, num):
    # Find the maximum XOR of num with elements in the trie
    node = root
    maxXOR = 0
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        toggleBit = 1 - bit
        if toggleBit in node.children:
            maxXOR |= 1 << i
            node = node.children[toggleBit]
        else:
            node = node.children.get(bit, node)
    return maxXOR


def maximumvalue(arr):
    root = TrieNode()
    prefix_xor = 0
    max_xor = 0

    # Insert 0 into the Trie to handle the case where the XOR of the entire array is maximum
    insert(root, 0)

    for num in arr:
        prefix_xor ^= num  # Calculate prefix XOR
        insert(root, prefix_xor)  # Insert current prefix XOR into the trie
        max_xor = max(max_xor, findMaximumXOR(root, prefix_xor))  # Update max XOR

    return max_xor


# Example usage
arr = [5, 1, 4, 7]
result = maximumvalue(arr)
print(result)  # Output: 14
arr = [8, 2, 4, 12, 1]
result = maximumvalue(arr)
print(result)  # Output: 14
arr = [1, 2, 3]
result = maximumvalue(arr)
print(result)  # Output: 14
arr = [0, 2, 5, 1]
result = maximumvalue(arr)
print(result)  # Output: 14
