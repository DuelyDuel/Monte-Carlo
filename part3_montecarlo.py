import math
import random
from scipy.stats import norm
import statistics
import matplotlib.pyplot as plt


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
    payoffs = []
    for i in range(n):
        S_T = simulate_price(S,r,sigma,T)
        a = max(S_T - K, 0)
        payoffs.append(a * math.exp(-r * T))
    price = sum(payoffs) / n
    standard_deviation = statistics.stdev(payoffs)
    standard_error = standard_deviation / math.sqrt(n)
    return price, standard_error


def bs_call(S, K, r, sigma, T):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

true_price = bs_call(100, 100, 0.05, 0.2, 1)
good_run = 0
for i in range(200):
    price, se = mc_call(100, 100, 0.05, 0.2, 1, 10000)
    if (price - 1.96 * se) < true_price < (price + 1.96 * se):
        good_run += 1

print(good_run / 200)
print("Mc call (price and standard error): ", mc_call(100, 100, 0.05, 0.2, 1, 1000000))
print("Bs call: ", bs_call(100, 100, 0.05, 0.2, 1))
price, se = mc_call(100, 100, 0.05, 0.2, 1, 100000)
print("Price:",price,"Standard Error: ", se)
print("95% Confidence Interval:", price - 1.96 * se, "to", price + 1.96 * se)

trial_counts = [100, 300, 1000, 3000, 10000, 30000, 100000]
prices = []
errors = []

for n in trial_counts:
    price, se = mc_call(100, 100, 0.05, 0.2, 1,n)
    prices.append(price)
    errors.append(se)

true_price = bs_call(100, 100, 0.05, 0.2, 1)

plt.errorbar(trial_counts, prices, yerr=[1.96 * s for s in errors], fmt="o-", capsize=4, label="Monte Carlo (95% CI)")
plt.axhline(true_price, linestyle="--", color="black", label="Black-Scholes")
plt.xscale("log")
plt.xlabel("Number of trials")
plt.ylabel("Call price")
plt.title("Monte Carlo convergence to Black-Scholes")
plt.legend()
plt.savefig("convergence.png", dpi=150)
plt.show()