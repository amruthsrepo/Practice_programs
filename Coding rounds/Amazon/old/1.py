def groceries(n, numProducts):
    if n < 3:
        if numProducts[0] < numProducts[1]:
            return sum(numProducts)
        return numProducts[1]
    l,r = 0,0
    while l < n-1:
        while r < len(numProducts)-1 and numProducts[r] < numProducts[r+1]:
            r += 1
        if r == l and r < (n-1):
            l,r = r+1, r+1
            continue
        numProducts[r] = sum(numProducts[l:r+1])
        numProductsL = numProducts[:l]
        numProductsR = numProducts[r:]
        numProductsL.extend(numProductsR)
        numProducts = numProductsL
        l = 0 if l==0 else l-1
        l,r = l,l
    return(max(numProducts))

print(groceries(4, [2,9,10,3,7]))
print(groceries(4, [20,13,8,9]))