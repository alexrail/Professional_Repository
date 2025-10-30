# Professional_Repository
Portfolio showcasing my work with AR Capital Partners LLC. Focused on quantitative research, financial modeling, and Python-based automation for trading, portfolio construction, and risk analysis. Highlights data-driven tools and systematic strategy development.

# PCA Portfolio Analysis (S&P 500)

This project applies **Principal Component Analysis (PCA)** to construct factor-based portfolios using **S&P 500 historical data**.  
It evaluates how eigenvector-derived weights perform relative to the index and volatility-scaled alternatives.

---

### Project Files
src/pca_portfolio.py # Core PCA model and data-fetching logic

results/pca_line_chart-10-20-2025.png # Updated equity curve (as of Oct 30, 2025)
results/Principle Component Analysis-10-20-2025.docx # Summary report and interpretation

### Overview
- **Portfolio 1 (Eigenvector Weights):** Tracks S&P 500 with lower volatility.  
- **Portfolio 2 (Eigenvector / Volatility Weights):** Over-weighted defensives → underperformance.  
- **Benchmark:** S&P 500 cumulative return for comparison.

---

### Notes
- Added request headers to fix 403 error when scraping S&P 500 tickers.  
- Updated analysis and visualizations through **October 30, 2025**.  
- Chart shows comparative cumulative returns of both PCA portfolios vs. S&P 500.

---

**Author:** Alexander Railton  
**Last Updated:** October 31, 2025