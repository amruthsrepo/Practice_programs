def countPurchases(cost, budget):

    numPurchases = 0
    sumPurchase = 0

    while budget:
        canPurchase = []
        prevBudget = budget

        for purchase in cost:
            if purchase <= budget:
                budget -= purchase
                numPurchases += 1
                sumPurchase += purchase
                canPurchase.append(purchase)
            if not budget:
                return numPurchases

        multiplePurchase = budget // sumPurchase
        numPurchases += multiplePurchase * sumPurchase

        cost = canPurchase

        if prevBudget == budget or not budget:
            return numPurchases

    return numPurchases


print(countPurchases([5, 8, 3], 12))
print(countPurchases([2, 4, 100, 2, 6], 21))
print(countPurchases([2, 2, 7, 5], 15))
