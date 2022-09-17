# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    # print('1')
    try:
        inputNodes = input().split(' ')
    except:
        print('E1')
        return
    childNodeMap = {}
    parentNodeMap = {}
    class Node(object):
        def __init__(self, letter = '', children = []):
            self.letter = letter
            self.children = children
    for pair in inputNodes:
        # print('yo', pair, len(pair))
        if len(pair) > 5:
            print('E1')
            return
        try:
            # print('yo1', pair)
            p,c = pair[1], pair[3]
            if c in childNodeMap.get(p,[]):
                print('E2')
                return
            childNodeMap[p] = childNodeMap.get(p,[])
            childNodeMap[p].append(c)
            parentNodeMap[c] = parentNodeMap.get(c,[])
            parentNodeMap[c].append(p)
            if len(childNodeMap[p]) > 2:
                print('E3')
                return
            if len(parentNodeMap[c]) > 1:
                print('E4')
                return
            if parentNodeMap[c] == p and parentNodeMap.get(p,[''])[0] == c:
                print('E5')
                return
            if childNodeMap[p] == c and childNodeMap.get(c,[''])[0] == p:
                print('E5')
                return
        except Exception as e:
            # print('yo2', str(e))
            print('E1')
            return
        # print(pair, childNodeMap, parentNodeMap)
    numCnotinP = 0
    for c in childNodeMap.keys():
        if c not in parentNodeMap:
            numCnotinP += 1
    numPnotinC = 0
    for p in parentNodeMap.keys():
        if p not in childNodeMap:
            numPnotinC += 1
    # print(numCnotinP, numPnotinC)
    if numPnotinC - numCnotinP > 1:
        print('E4')
        return
    def recursiveNodeAdd(nodeString, parent):
        for c in childNodeMap.get(parent, []):
            nodeString = recursiveNodeAdd(nodeString + '(' + c, c)
        return nodeString + ')'
    print(recursiveNodeAdd('('+inputNodes[0][1], inputNodes[0][1]))
main()