import yfinance as yf
import datetime


start = datetime.datetime(2021,7,1)
end = datetime.datetime(2021,7,29)
try:
    etfs = ['VCN.TO', 'VUN.TO', 'VIU.TO', 'VEE.TO']
    bonds = ['VBU.TO', 'VBG.TO']

    etf = yf.download(etfs,start=start, end=end, progress=False)["Close"]
    bond = yf.download(bonds,start=start, end=end, progress=False)["Close"]
except Exception:
    None

#print(etf)
#print(bond)