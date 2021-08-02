# At the end couldn't manage to finish on time
import yfinance as yf

amount = input("Enter the amount you wish to invest: ")
risk = input("Enter a number from 1 to 5, indicating the risk level you'd like to take with your investment: "(period="1y")
vunHist = yf.Ticker("VUN.TO").history(period="1y")
viuHist = yf.Ticker("VIU.TO").history(period="1y")
veeHist = yf.Ticker("VEE.TO").history(period="1y")
vbuHist = yf.Ticker("VBU.TO").history(period="1y")
vbgHist = yf.Ticker("VBG.TO").history(period="1y")


price_data = [vcnHist["Close"]]

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
        variance = j - meanPercentChange[i]2
        variances.append(variance)
    variances_list.append(variances)

volatilities_list = []
volatilities=[]

for i in range(len(variances_list)):
    for j in variances_list[i]:
        volatility = (abs(j)(1/2))*250
        volatilities.append(volatility)
    volatilities_list.append(volatilities)
print(volatilities_list[-1])

meanVolatility = sum(volatilities)/len(volatilities)
print(meanVolatility)