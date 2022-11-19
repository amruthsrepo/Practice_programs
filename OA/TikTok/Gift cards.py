# def way2buy(nCard,cost,denomList=[],returnSet):
#     if not nCard: return 0
#     returnSet = set()
#     count = 0
#     denom = [10, 30, 50]
#     for d in denom:
#         if cost == d:
#             returnSet.add(tuple([[denomList]+[d]].sort()))
#         else:
#             count += way2buy(nCard-1, cost-d)
#     return count + returnSet

# nCard, cost = [int(_n) for _n in input().split(' ')]
# print(way2buy(nCard, cost))


import itertools #importing library

def way2buy (num_of_card, total_cost): #User-defined function to return the number of ways to buy the item

    denomination = [10,30,50] # Available denominations are $10, 30 and 50 
    result = set() #Variable to store all combinations with replacement 
    count = 0 #Variable to count the correct way to buy the item

    for c in itertools.combinations (denomination, len (denomination)): #store all possible combinations

        result.update(itertools.combinations_with_replacement (c, num_of_card)) 
    for _ in result: # Filter correct cobinacombinationstions 
        if sum(_) == total_cost: 
            count += 1

    return count #Return the number of ways

input_list = input().split() #Take two space-separated integer as 
num_of_card = int(input_list [0]) #varible to store total number of cards = 
total_cost = int(input_list[1]) #variable to store total cost of item 
print(way2buy (num_of_card, total_cost)) #Calling Way2the Buy function to print the total way to buy an item with given the en cost