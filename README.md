# Monte Carlo Option Pricing

A Python project where I price options with Monte Carlo simulation and check the results against the Black-Scholes formula. I'm building it step by step as I learn quantitative finance at Baruch College.

## What's in here

- `part1_ev.py` – Simulating an expected-value dice game: roll a die, keep it or reroll.
- `part1b_ev.py` – Exact expected value with k rerolls (computed by working backward), and a recursive simulation that plays the optimal strategy. The simulation matches the exact answer to within about 0.005 for up to 5 rerolls.
- `part2_blackscholes.py` – The Black-Scholes closed-form price for a European call.
- `part3_montecarlo.py` – Monte Carlo pricer: simulates final stock prices under geometric Brownian motion, averages the discounted call payoffs, and reports a standard error and 95% confidence interval.

## Results

Test option: S = 100, K = 100, r = 5%, σ = 20%, T = 1 year.

| Method | Price |
|---|---|
| Black-Scholes (exact) | 10.4506 |
| Monte Carlo, 1,000,000 trials | 10.449 (standard error 0.015) |

- The standard error fell from 0.046 at 100,000 trials to 0.015 at 1,000,000, which matches the 1/√n rule.
- **Coverage test:** I ran the pricer 200 times (10,000 trials each) and checked whether the 95% confidence interval contained the Black-Scholes price. It did in 95% of runs.

## How it works

The simulated stock price at expiration is:

S_T = S · exp((r − ½σ²)T + σ√T · Z), where Z is a standard normal random draw.

The call price is the average of max(S_T − K, 0) over all simulations, discounted by e^(−rT).

## What's next

- Convergence plots
- Variance reduction (antithetic and control variates)
- Greeks by simulation
- Asian and barrier options, which have no simple closed form
- Real market data and implied volatility

## Limitations

Black-Scholes and this simulation assume constant volatility and a risk-free rate, and no jumps. Real markets don't behave that way.
