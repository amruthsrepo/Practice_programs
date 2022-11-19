# def getUncleanedStreets(m , n, arrStart, arrEnd): 
#     streets = [] 
#     for i in range(n): 
#         streets.append(i) 
#         for i in range(m): 
#             for j in range(arrStart[i], arrEnd[i]+1): 
#                 if j in streets: streets.remove(j) 
#                 return len(streets) 

# string = input() 
# splitted = string.split() 
# m = int(splitted[0]) 
# n = int(splitted[1]) 
# arrStart = [] 
# arrEnd = [] 
# for i in range(m): 
#     string = input() 
#     splitted = string.split() 
#     arrStart.append(int(splitted[0])) 
#     arrEnd.append(int(splitted[1])) 

# print(getUncleanedStreets(m,n,arrStart,arrEnd)) 


nWork, nStreet = [int(_n) for _n in input().split(' ')]
setTasks = []
for n in range(nWork):
    setTasks.append([int(_n) for _n in input().split(' ')])
setTasks.sort(key= lambda x: x[0])
combinedTasks = []
prevStart, prevEnd = setTasks[0]
for start,end in setTasks[1:]:
    print(start,end)
    if start <= prevEnd:
        prevEnd = max(end, prevEnd)
    else:
        combinedTasks.append((prevStart,prevEnd))
        prevStart,prevEnd = start,end
combinedTasks.append((prevStart,prevEnd))
s1,e1 = combinedTasks[0]
buggyStreets = s1
for s2,e2 in combinedTasks[1:]:
    buggyStreets += (s2-e1-1)
    s1,e1 = s2,e2
print(buggyStreets+(nStreet-e1-1))