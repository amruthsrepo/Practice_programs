def find_last_round_trip(trips, a2b, b2a):
    ct = 0
    
    for _ in range(trips):
        for ab in a2b:
            if ab >= ct:
                break
        
        ct = ab + 100
        
        for ba in b2a:
            if ba >= ct:
                break
        
        ct = ba + 100
    
    return ct








a2b = [50, 200, 400]
b2a = [100, 300, 500]
trips = 2
result = find_last_round_trip(trips, a2b, b2a)

a2b = [0, 200, 500]
b2a = [99, 210, 450]
trips = 1
result = find_last_round_trip(trips, a2b, b2a)

a2b = [109,200,500]
b2a = [99,210,600]
trips = 2
result = find_last_round_trip(trips, a2b, b2a)

a2b = [5,206]
b2a = [105,306]
trips = 2
result = find_last_round_trip(trips, a2b, b2a)
