import numpy as np
import pandas as pd
import cvxpy as cp
import matplotlib.pyplot as plt
import yfinance as yf

TRADING_DAYS = 252
tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", 
           "JPM", "V", "XOM", "UNH", "META"]
start_date = "2023-01-01"
end_date = "2025-11-01"

# --- Download data ---
data = yf.download(tickers, start=start_date, end=end_date)

# Handle multi-index or flat columns
if isinstance(data.columns, pd.MultiIndex):
    if "Adj Close" in data.columns.get_level_values(0):
        data = data["Adj Close"]
    elif "Close" in data.columns.get_level_values(0):
        data = data["Close"]
else:
    if "Adj Close" in data.columns:
        data = data["Adj Close"]
    elif "Close" in data.columns:
        data = data["Close"]

# --- Compute daily returns and statistics ---
returns = data.pct_change().dropna()
mu = returns.mean().values
Sigma = returns.cov().values
n = len(mu)

print(f"Data pulled for {n} assets from {start_date} to {end_date}")
print("Average daily returns:", np.round(mu, 5))

# --- Efficient Frontier ---
frontier_weights, frontier_risks, frontier_returns = [], [], []
target_returns = np.linspace(mu.min(), mu.max() * 1.3, 200)

for t in target_returns:
    w = cp.Variable(n)
    risk = cp.quad_form(w, Sigma)
    ret = mu @ w
    constraints = [cp.sum(w) == 1, w >= 0, w <= 0.3, ret >= t]
    prob = cp.Problem(cp.Minimize(risk), constraints)
    prob.solve()
    if w.value is not None:
        w_opt = w.value
        frontier_weights.append(w_opt)
        frontier_returns.append(mu @ w_opt)
        frontier_risks.append(np.sqrt(w_opt.T @ Sigma @ w_opt))

frontier_returns, frontier_risks = np.array(frontier_returns), np.array(frontier_risks)

# --- Equal Weight Portfolio ---
w_equal = np.ones(n) / n
risk_equal = np.sqrt(w_equal.T @ Sigma @ w_equal)
ret_equal = mu @ w_equal
rf = 0.0001  # daily risk-free rate
sharpe_equal = (ret_equal - rf) / risk_equal

print("\nEqual Weights Portfolio:")
print("Expected return:", np.round(ret_equal, 4))
print("Risk (stdev):", np.round(risk_equal, 4))
print("Sharpe:", np.round(sharpe_equal, 3))

# --- Tangent Portfolio (Derived from Frontier) ---
sharpe_arr = (frontier_returns - rf) / frontier_risks
idx_tan = np.argmax(sharpe_arr)
tan_ret, tan_risk, sharpe_ratio = frontier_returns[idx_tan], frontier_risks[idx_tan], sharpe_arr[idx_tan]
w_tangent = frontier_weights[idx_tan]

print("\nTangent Portfolio (Derived from Frontier):")
print("Weights:", np.round(w_tangent, 3))
print(f"Expected Return: {tan_ret:.5f}")
print(f"Risk (Std Dev): {tan_risk:.5f}")
print(f"Sharpe Ratio: {sharpe_ratio:.3f}")

# --- Annualization ---
annual_ret_equal = ret_equal * TRADING_DAYS
annual_risk_equal = risk_equal * np.sqrt(TRADING_DAYS)
annual_ret_tan = tan_ret * TRADING_DAYS
annual_risk_tan = tan_risk * np.sqrt(TRADING_DAYS)
rf_annual = rf * TRADING_DAYS
annual_sharpe_equal = (annual_ret_equal - rf_annual) / annual_risk_equal
annual_sharpe_tan = (annual_ret_tan - rf_annual) / annual_risk_tan

# --- Print Summary ---
print("\nAnnualized Equal Weight Portfolio:")
print(f"Return: {annual_ret_equal:.2%}, Risk: {annual_risk_equal:.2%},  Sharpe: {annual_sharpe_equal:.3f}")
print("\nAnnualized Tangent Portfolio:")
print(f"Return: {annual_ret_tan:.2%}, Risk: {annual_risk_tan:.2%}, Sharpe: {annual_sharpe_tan:.3f}")

# --- Plot Efficient Frontier ---
frontier_returns_annual = frontier_returns * TRADING_DAYS
frontier_risks_annual = frontier_risks * np.sqrt(TRADING_DAYS)

plt.figure(figsize=(9,6))
plt.plot(frontier_risks_annual, frontier_returns_annual, 'b--', label='Efficient Frontier')
plt.scatter(annual_risk_equal, annual_ret_equal, color='red', s=80, label='Equal Weight')
plt.scatter(annual_risk_tan, annual_ret_tan, color='green', s=120, marker='*', label='Tangent Portfolio')
plt.annotate('Tangent Portfolio',
             xy=(annual_risk_tan, annual_ret_tan),
             xytext=(annual_risk_tan+0.01, annual_ret_tan+0.03),
             arrowprops=dict(arrowstyle='->', color='black'))

# Capital Market Line
x = np.linspace(0, max(frontier_risks_annual)*1.05, 100)
cml = rf_annual + annual_sharpe_tan * x
plt.plot(x, cml, 'k--', label='Capital Market Line')

plt.title('Efficient Frontier, Tangent Portfolio & CML (Annualized)')
plt.xlabel('Annualized Risk (Standard Deviation)')
plt.ylabel('Annualized Expected Return')
plt.legend()
plt.grid(True)
plt.show()
