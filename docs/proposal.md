# Diversified Stock Price Prediction Using Deep Learning: A Sector-Based Approach for Enhanced Investment Strategies

## Title and Author
**Title**: Diversified Stock Price Prediction Using Deep Learning: A Sector-Based Approach for Enhanced Investment Strategies 
**Author**: Esther Priyadarshini  

**Links**:
- GitHub: [https://github.com/ESTHER-PRIYADARSHINI/UMBC-DATA606-Capstone](https://github.com/ESTHER-PRIYADARSHINI/UMBC-DATA606-Capstone)
- LinkedIn: [https://www.linkedin.com/in/estherpriyadarshini/](https://www.linkedin.com/in/estherpriyadarshini/)
- PowerPoint and YouTube: (To be added after completion)

## Background
**Topic**: Diversified Stock Price Prediction Using Deep Learning: A Sector-Based Approach for Enhanced Investment Strategies

### What is it about?
This project aims to leverage advanced machine learning techniques, specifically a stacked Long Short-Term Memory (LSTM) model, to predict and forecast stock prices for companies from different sectors. The selected companies—Coca-Cola (consumer goods), Apple (technology), Amazon (e-commerce/technology), Pfizer (healthcare), Chevron (energy), and Tesla (automotive)—are industry leaders, making them crucial for investors aiming to diversify their portfolios. By predicting future stock prices accurately, investors can make informed decisions, minimize risk, and maximize returns.

### Why does it matter?
Stock price prediction is a highly valuable tool in financial markets. The ability to forecast future stock prices can provide a competitive edge to investors and traders. More accurate predictions enable informed decision-making, mitigating the impact of market volatility and sector-specific risks. By predicting across multiple sectors, this project will showcase the advantages of diversification, where investors can distribute their investments across different industries to reduce the overall risk associated with downturns in specific sectors.

In an ever-growing global economy, industries can fluctuate due to external factors like economic policies, political events, or natural disasters. For instance, while the healthcare sector may see a surge during a global health crisis, the automotive or energy sectors could face challenges. Predicting stock prices across these diverse industries can help minimize the risk of significant losses when one industry faces a downturn. This approach offers a broader, more reliable view for investors looking to grow their portfolios, regardless of market conditions.

### Research Questions
1. Can a stacked LSTM model provide more accurate stock price predictions than traditional models?
2. How do stock price trends differ across diverse sectors, such as technology, healthcare, consumer goods, energy, and automotive?
3. Can machine learning-based stock price predictions provide actionable insights for investors to diversify their portfolios and reduce risk?
4. How can predictive models be enhanced to give new or inexperienced investors confidence in their investment decisions?

The purpose of this project is to explore how deep learning models, specifically stacked LSTMs, can be applied to predict stock prices and how these predictions can aid investors in balancing their portfolios. With machine learning models becoming increasingly sophisticated, accurate stock price predictions have the potential to revolutionize both personal and institutional trading strategies, contributing to the stability and growth of financial markets.

## Data

### Data Sources
The datasets used in this project comprise historical stock prices for six major companies from different sectors: Coca-Cola (consumer goods), Apple (technology), Amazon (e-commerce/technology), Pfizer (healthcare), Chevron (energy), and Tesla (automotive). The data has been sourced from Yahoo Finance, accessed via the `yfinance` API, covering a period of 20 years (2003 to 2023).

### Data Size
The individual CSV files for each company vary in size but are approximately 0.55 MB each. For six companies, the total data size aggregates to approximately 3.3 MB.

### Data Shape
Each CSV file contains approximately 5034 rows and 7 columns. Combined, the total data shape can be represented as follows:
- **Total number of rows**: 30,204 (5034 rows per file × 6 files)
- **Number of columns**: 7 per file

### Time Period
The data spans a period from 2004-09-01 to 2024-08-30, providing a comprehensive historical view of stock prices for each company over 20 years.

### Row Representation
Each row represents daily stock prices for a particular stock.

### Data Dictionary
- **Date**: Date of the stock price.
- **Open**: Opening price.
- **Close**: Closing price.
- **High**: Highest price of the day.
- **Low**: Lowest price of the day.
- **Volume**: Volume of shares traded.

### Target and Features
- **Target**: Predict future `Close` prices.
- **Features**: 
  - `Volume`
  - `Open`
  - `High`
  - `Low`
  - Moving averages
