import math
from scipy.stats import norm

def bs_call(S,K,r,sigma,T):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

print(bs_call(100,100,0.05,0.2,1))