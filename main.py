from flask import request,Flask,app,jsonify,render_template


app = Flask(__name__)



@app.route('/',methods=['GET','POST'])

def init():
    if request.method == 'POST':
        investment = request.form.get('investment')
        time = request.form.get('time')
        risk = request.form.get('risk')
        print(investment,time,risk)

        return render_template("suggest.html")

    else:
        return render_template("base.html")

app.run(host='0.0.0.0',port=5000,debug=True)

