import math
import random

def simulate_price(S,r,sigma,T):
    Z = random.gauss(0,1)
    S_T = S * math.exp((r - 0.5 * sigma**2) * T + sigma *math.sqrt(T) * Z)
    return S_T


def average_price(n):
    total = 0
    for i in range(n):
        total += simulate_price(100, 0.05, 0.2, 1)
    return (total/n)

def mc_call(S,K,r,sigma,T,n):
    total = 0
    for i in range(n):
        S_T = simulate_price(S,r,sigma,T)
        a = max(S_T - K, 0)
        total += a
    return (total / n) * math.exp(-r * T)

print(mc_call(100, 100, 0.05, 0.2, 1, 1000000))
