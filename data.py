import yfinance as yf
import datetime


start = datetime.datetime(2021,7,1)
end = datetime.datetime(2021,7,29)
try:
    stock = []
    stock = yf.download('FB',start=start, end=end, progress=False)
except Exception:
    None

print(stock)