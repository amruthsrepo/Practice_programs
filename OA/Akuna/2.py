def generate_sequence(n):
    sequence = [1]

    for _ in range(n - 1):
        current_number = sequence[-1]
        count = 1
        next_number = 0
        multiplier = 10

        while current_number > 0:
            digit = current_number % 10
            current_number //= 10

            if current_number % 10 == digit:
                count += 1
            else:
                next_number += count * multiplier + digit
                count = 1
                multiplier *= 10

        next_number += count * multiplier
        sequence.append(next_number)

    return sequence


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def find_sequence_sums(queries):
    result = []

    max_query = max(queries)
    sequence = generate_sequence(max_query)

    for query in queries:
        result.append(sum_of_digits(sequence[query - 1]))

    return result


# Example usage:
input_queries = [1, 2, 3, 4, 5, 6, 7]
output = find_sequence_sums(input_queries)
print(output)


# print(sumOfTheDigits([20]))
# print(sumOfTheDigits([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(sumOfTheDigits([100, 1, 2, 3, 4, 5]))
# print(sumOfTheDigits([1000, 1, 2, 3, 4, 5]))
