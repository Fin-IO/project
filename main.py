from flask import request,Flask,app,jsonify,render_template

from data import etf, bond

app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def init():
    if request.method == 'POST':
        investment = request.form.get('investment')
        time = request.form.get('time')
        risk = request.form.get('risk')
        print(investment,time,risk)
        data=[{"symbol":'VCN.TO',"name":"Vanguard FTSE Canada All Cap Index ETF","asset":"ETFs","price":41.02,"_shares":4},
        {"symbol":'VUN.TO',"name":"Vanguard U.S. Total Market Index ETF","asset":"ETFs","price":76.87,"_shares":4},
        {"symbol":'VIU.TO',"name":"Vanguard FTSE Developed All Cap Ex North America Index ETF","asset":"ETFs","price":32.37,"_shares":4}]
        return render_template("suggest.html",data=data)

    else:
        return render_template("input.html")

@app.route('/graph/v')
def graph():
    return render_template('graph.html')

app.run(host='0.0.0.0',port=5000,debug=True)

