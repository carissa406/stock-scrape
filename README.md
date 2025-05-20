# 📈 MarketWatch Stock Scraper

This Python script scrapes basic stock information from [MarketWatch](https://www.marketwatch.com) for a list of predefined tickers and exports the results into a CSV file.

## 🔍 What It Does

For each stock symbol in your list, the script collects:

- **Current stock price**
- **Dividend yield (%)**

The data is compiled into a structured table and saved as `stocks.csv`.

## 🧪 Example Output

| Stock | StockPriceClose | Div% |
|-------|------------------|------|
| F     | 12.45            | 4.87 |
| KMI   | 17.65            | 6.31 |

*(Example values only)*

## ⚙️ Tech Stack

- Python 3.x  
- [Requests](https://pypi.org/project/requests/)  
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)  
- [Pandas](https://pypi.org/project/pandas/)

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/marketwatch-stock-scraper.git
   cd marketwatch-stock-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python stock_scraper.py
   ```

4. Output:
   - A `stocks.csv` file will be created in the current directory.

## 📝 Customization

To scrape different stocks, update the `STOCKS` list at the top of `stock_scraper.py`:
```python
STOCKS = ['AAPL', 'MSFT', 'GOOG']
```

## 📄 Notes

- The script depends on the current structure of MarketWatch pages. If the HTML structure changes, the scraping logic may need to be updated.
- Avoid sending too many requests in a short time to prevent IP blocking.
