import random

def play_once():
    first = random.randint(1,6)
    if first >= 4:
        return first
    return random.randint(1,6)
def play_twice():
    first = random.randint(1,6)
    if first >= 5:
        return first
    return play_once()
def play_thrice():
    first = random.randint(1,6)
    if first >= 5:
        return first
    return play_twice()
def estimate_ev(n):
    total = 0
    for i in range(n):
        total += play_thrice()
    return total/n

print(estimate_ev(100000))
