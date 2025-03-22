from collections import Counter


def min_operations(n, locations):
    location_counts = Counter(locations)  # Count occurrences of each location
    num_oper = 0

    while location_counts.keys():
        for k in location_counts.keys():
            location_counts

    unique_locations = len(location_counts)  # Number of unique locations
    total_products = sum(location_counts.values())  # Total number of products

    # If we have at least two unique locations, we can always pair them up
    # The minimum number of operations is calculated as:
    min_ops = max(unique_locations, (total_products + 1) // 2)

    return min_ops


# Example usage
n = 5
locations = [1, 8, 6, 7, 7]
print(min_operations(n, locations))  # Output: 3
