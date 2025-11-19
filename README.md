# 🚀 Professional_Repository
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Last Updated](https://img.shields.io/badge/Updated-Nov%202025-lightgrey.svg)

Portfolio highlighting quantitative modeling, algorithmic research, and full-stack development across Python, SQL, and C++.
Includes AI/ML implementations, financial time-series forecasting, risk analytics, and engineered tooling for systematic trading and portfolio optimization.

# 🧠 About AR Capital Partners LLC

**AR Capital Partners LLC** is a quantitative research and financial engineering practice focused on:


- **Quantitative Model Development** — risk models, alpha signals, PCA analysis, statistical factor models  
- **Financial Forecasting & Time Series Modeling** — ARIMA/SARIMAX, volatility forecasting, seasonality analysis  
- **Portfolio Construction & Optimization** — Markowitz/CVXPy optimizers, risk budgeting, factor- and beta-neutral portfolios  
- **Risk & Scenario Analytics** — Monte Carlo simulation, VaR/ES, stress testing frameworks  
- **Machine Learning for Finance** — predictive modeling, anomaly detection, ML-based forecasting  
- **NLP & Document Automation** — automated model documentation, filings extraction, MRM workflow tools  
- **Financial Data Engineering** — scraping, API ingestion, ETL pipelines, factor dataset creation  
- **Backtesting & Research Automation** — systematic strategy frameworks, performance attribution tools  
- **Model Validation & MRM Consulting** — SR 11-7 compliant validation, benchmark reconstruction, documentation  
- **Python Engineering for Quant Workflows** — production-quality research tools and automation scripts


This repository highlights production-grade research, models, and tools developed for internal use.

---

# 📊 PCA Portfolio Analysis (S&P 500)

<details>
<summary><strong>Click to expand</strong></summary>

Applies **Principal Component Analysis (PCA)** to build factor-derived equity portfolios using historical **S&P 500** data.

### 🔍 Overview
- **Portfolio 1 — Eigenvector Weights:**  
  Tracks S&P 500 with lower volatility.
- **Portfolio 2 — Eigenvector / Volatility Weights:**  
  Defensive tilt → relative underperformance.
- **Benchmark:** S&P 500 cumulative return.

### 📁 Project Files
- `src/pca_portfolio/`  
- `results/pca_portfolio/pca_line_chart-10-20-2025.png`  
- `results/pca_portfolio/Principal Component Analysis-10-20-2025.docx`

### 📝 Notes
- Added headers to bypass 403 errors when fetching tickers  
- Updated through **October 30, 2025**

</details>

---

# 📈 Statistical Factor Models (Equity Factors)

<details>
<summary><strong>Click to expand</strong></summary>

Implements a full **statistical factor modeling** pipeline across equities:

### 🔍 Features
- Cross-sectional and time-series factor regressions  
- Fama–French-style multi-factor modeling  
- Sector-neutral and beta-neutral factor portfolios  
- Rolling window regressions & factor stability analysis  
- Factor return attribution and risk decomposition  

### 📁 Project Files
- `src/stat_factor_models/`  
- `results/stat_factor_analysis/`

</details>

---

# 📉 Portfolio Optimization (Markowitz + CVXPy)

<details>
<summary><strong>Click to expand</strong></summary>

Comprehensive portfolio optimization toolkit using classical and modern methods:

### 🔍 Optimization Methods
- Mean-variance optimization (Markowitz)  
- Efficient frontier computation  
- CVXPy-based quadratic optimization  
- Volatility targets & risk budgeting  
- Leverage constraints, sector constraints, long-only portfolios  

### 📁 Project Files
- `src/portfolio_optimization/optimizer.py`  
- `results/portfolio_optimization/efficient_frontier.png`  
- `results/portfolio_optimization/report.docx`

</details>

---

# 📘 Time Series Modeling & Monte Carlo Simulation

<details>
<summary><strong>Click to expand</strong></summary>

A complete notebook demonstrating time-series forecasting & simulation:

### 🔍 Methods Included
- ARIMA & SARIMAX modeling  
- ACF/PACF analysis and decomposition  
- Residual diagnostics (Ljung–Box, JB test, heteroskedasticity tests)  
- Monte Carlo simulation with drift adjustment  
- Confidence interval estimation  
- Full path simulation for scenario analysis  

### 📁 Project Files
- `Time Series Modeling and Monte Carlo Simulation/TimeSeries_Modeling_and_MonteCarlo.ipynb`

</details>

---

# 🧪 Technical Stack

- **Python:** NumPy, Pandas, Statsmodels, CVXPY, Scikit-learn, ARCH  
- **Visualization:** Matplotlib, Seaborn  
- **Data:** yFinance, custom scrapers, historical S&P 500 data  
- **Reports:** PNG charts, DOCX summaries, Jupyter notebooks  

---

# 👤 Author
**Alexander Railton**  
Founder & Quantitative Researcher — AR Capital Partners LLC  
📍 United States  
🕒 Last Updated: **November 2025**

