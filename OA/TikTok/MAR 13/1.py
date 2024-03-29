# Implement an algorithm to hash a URL as described.
# Suppose the given URL url of length n is to be hashed with a string hash_string of length m. Given an integer k, run the url through the following algorithm:
# 1. Divide the URL into blocks of size k starting from the left. The last block can be smaller than k. For example, if url = "https://xyz.com"and k = 4, the blocks are ["http", "s://", "xyz.", "com"].
# 2. The values of the English characters 'a', 'b',... Z' are 0, 1, .., 25 respectively, and that of ':', '/' and '.' are 26, 27, and 28 respectively. Thus the has value of the block "s://" will be 19 + 26 + 27 + 27 = 98.
# 3. For each URL, find the hash value of each block. The hash value is the sum of the values of each character.
# 4. Replace the block with the (hash value of the block modulo with character of the string hash_string.


def getHashedURL(url, hash_string, k):

    returnString = ""
    hashLen = len(hash_string)
    ordA = ord("a")
    symbolOrd = {":": 26, "/": 27, ".": 28}

    for i in range(0, len(url), k):
        currHash = 0
        for j in range(i, i + k):
            if j == len(url):
                break
            if url[j] in symbolOrd:
                currHash += symbolOrd[url[j]]
            else:
                currHash += ord(url[j]) - ordA
        currHash %= hashLen
        returnString += hash_string[currHash]

    return returnString


url = "https://xyz.com"
hash_string = "pqrst"
k = 4
print(getHashedURL(url, hash_string, k))  # a

url = "https://caayxdycdzwxwac.com"
hash_string = "awpixaia"
k = 7
print(getHashedURL(url, hash_string, k))  # a

url = "https://bet/addg/.com"
hash_string = "gsuljpbokkkd"
k = 4
print(getHashedURL(url, hash_string, k))  # a
