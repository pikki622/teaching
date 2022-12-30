import yfinance as yf

ticker = 'TWTR'
expiry = "2020-03-20"
data = yf.Ticker(ticker)
opt = data.option_chain(expiry)

opt.calls.to_csv(f"{ticker}_calls.csv")
opt.puts.to_csv(f"{ticker}_puts.csv")