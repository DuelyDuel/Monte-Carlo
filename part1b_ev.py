import random

def exact_ev(k):
    value = 3.5
    for i in range(k):                
        total = 0
        for face in range(1, 7):
            total += max(face,value)
        value = total/6
    return value
for k in range(6):
    print(k, exact_ev(k))

def play(rerolls):
    roll = random.randint(1,6)
    if rerolls == 0:
        return roll
    if roll > exact_ev(rerolls- 1):
        return roll
    return play(rerolls - 1)

def estimate_play(rerolls,n):
    total = 0
    for i in range(n):
        total += play(rerolls)
    return total/n

for k in range(6):
    print(k, estimate_play(k, 100000), exact_ev(k))