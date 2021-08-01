import yfinance as yf
import datetime


start = datetime.datetime(2021,7,1)
end = datetime.datetime(2021,7,29)
try:
    etfs = ['VCN', 'VUN', 'VIU', 'VEE']
    bonds = ['VBU', 'VBG']

    etf = yf.download('SPY IVV QQQ',start=start, end=end, progress=False)
except Exception:
    None

print(etf)