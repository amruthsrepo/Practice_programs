# def find_segments_after_destruction(houses, queries):
#     houses = sorted(houses)
#     houseSet = set(houses)
    
#     def countSegments(houses):
#         segments = 0
#         n = len(houses)
#         for i in range(n):
#             if i == 0 or houses[i] != houses[i - 1] + 1:
#                 segments += 1
#         return segments
    
#     segments = countSegments(houses)
#     result = []
    
#     for query in queries:
#         houseSet.remove(query)
#         houses = sorted(houseSet)
#         segments = countSegments(houses)
#         result.append(segments)
    
#     return result


def find_segments_after_destruction(houses, queries):
    # Sort the houses initially
    houses.sort()
    
    # Initialize the result list
    result = []
    
    # Keep track of house positions in a set for O(1) lookups
    house_set = set(houses)
    
    # Initially count the number of segments
    segments = 1
    for i in range(1, len(houses)):
        if houses[i] != houses[i - 1] + 1:
            segments += 1
    
    # Process each query (house destruction)
    for query in queries:
        house_set.remove(query)
        
        # Check the neighbors of the destroyed house
        left_neighbor = query - 1
        right_neighbor = query + 1
        
        left_exists = left_neighbor in house_set
        right_exists = right_neighbor in house_set
        
        # If the house being destroyed has no neighbors or both neighbors are separated
        if not left_exists and not right_exists:
            # This house was forming its own segment, so reduce segment count by 1
            segments -= 1
        elif left_exists and right_exists:
            # The house was connecting two segments, now those segments are merged into one
            segments += 1
        
        # Append the current number of segments after this destruction
        result.append(segments)
    
    return result





houses = [1, 2, 3, 6, 7, 9]
queries = [6, 3, 7, 2, 9, 1]
result = find_segments_after_destruction(houses, queries)
print(result)  


houses = [1, 2, 3, 6, 7, 10]
queries = [3, 7, 2, 6]

result = find_segments_after_destruction(houses, queries)
print(result)  

houses = [2, 4, 5, 6, 7]
queries = [5, 6, 2]

result = find_segments_after_destruction(houses, queries)
print(result)  
