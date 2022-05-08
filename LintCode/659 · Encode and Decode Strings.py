class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ''
        for s in strs:
            encoded += s + '`~'
        return encoded[:-2]

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        return None if not str else str.split('`~')