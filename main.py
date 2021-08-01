from flask import request,Flask,app,jsonify,render_template

from data import etf

app = Flask(__name__)



@app.route('/',methods=['GET','POST'])

def init():
    if request.method == 'POST':
        investment = request.form.get('investment')
        time = request.form.get('time')
        risk = request.form.get('risk')
        print(investment,time,risk)
        data=[{"symbol":'VCN',"name":"Vanguard FTSE Canada All Cap Index ETF","asset":"ETFs","price":41.02,"_shares":4},
        {"symbol":'VUN',"name":"Vanguard U.S. Total Market Index ETF","asset":"ETFs","price":76.87,"_shares":4},
        {"symbol":'VIU',"name":"Vanguard FTSE Developed All Cap Ex North America Index ETF","asset":"ETFs","price":32.37,"_shares":4}]
        return render_template("suggest.html",data=data)

    else:
        return render_template("base.html")

app.run(host='0.0.0.0',port=5000,debug=True)

