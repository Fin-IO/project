import yfinance as yf

tickers = ['VCN.TO', 'VUN.TO', 'VIU.TO', 'VEE.TO', 'VBU.TO', 'VBG.TO']

vcnHist = yf.Ticker("VCN.TO").history(period="1y")
vunHist = yf.Ticker("VUN.TO").history(period="1y")
viuHist = yf.Ticker("VIU.TO").history(period="1y")
veeHist = yf.Ticker("VEE.TO").history(period="1y")
vbuHist = yf.Ticker("VBU.TO").history(period="1y")
vbgHist = yf.Ticker("VBG.TO").history(period="1y")


price_data = [vcnHist["Close"], vunHist["Close"], viuHist["Close"], veeHist["Close"], vbuHist["Close"],
vbgHist["Close"]]

percentChange = []

for i in range(0, len(price_data), 1):
    list=[]
    prev=price_data[i][0]
    for j in price_data[i]:
        percent = (j - prev)/prev
        prev=j
        list.append(percent)
    percentChange.append(list)

# print(percentChange[1])

#Calculate Mean Perentage Change
meanPercentChange=[]
for i in percentChange:
    sum=0
    for percents in i:
        sum+=percents
    meanPercentChange.append(sum/len(percentChange))

# print(meanPercentChange)
variances_list = []
variances=[]

for i in range(len(percentChange)):
    for j in percentChange[i]:
        variance = j - meanPercentChange[i]**2
        variances.append(variance)
    variances_list.append(variances)
# print(variances_list)


volatilities_list = []
volatilities=[]

for i in range(len(variances_list)):
    for j in variances_list[i]:
        volatility = (j**(1/2))*250
        volatilities.append(volatility)
    volatilities_list.append(volatilities)
print(volatilities_list[-1])


