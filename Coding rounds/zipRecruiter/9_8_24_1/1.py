def construct_array(a):
    result = []
    
    n = len(a)
    
    for i in range(n):
        first_char = a[i][0]
        
        last_char = a[(i + 1) % n][-1]
        
        result.append(first_char + last_char)
    
    return result




    
a = ["apple", "banana", "cherry"]
output = construct_array(a)

a = ["cat", "dog", "ferret", "scorpion"]
output = construct_array(a)

a = ["I", "have", "a", "nice", "surprise"]
output = construct_array(a)
