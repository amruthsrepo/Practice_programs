def winner(erica, bob):
    erica_points = 0
    bob_points = 0
    points = {"E": 1, "M": 3, "H": 5}
    for i in range(len(erica)):
        erica_points += points[erica[i]]
        bob_points += points[bob[i]]
    if erica_points > bob_points:
        return "Erica"
    elif erica_points < bob_points:
        return "Bob"
    else:
        return "Tie"
