def packageDelivery(location, movedFrom, movedTo):
    location = set(location)
    for i in range(len(movedFrom)):
        location.remove(movedFrom[i])
        location.add(movedTo[i])
    location = list(location)
    location.sort()
    return location

print(packageDelivery([1,7,6,8],[1,7,2],[2,9,5]))