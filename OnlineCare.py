from logging import debug
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


app.config['SECRET_KEY'] = '4cf0ac173653f712733ee5a14a536acc'
@app.route("/")
def Welcome() :
    return render_template('wel.html')

@app.route("/register", methods=['GET', 'POST'])
def Reg() :
    if request.method == 'POST':
        flash(f'Registered Successfully!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('register.html')
    

@app.route("/signin", methods=['GET', 'POST'])
def Sign() :
    if request.method == 'POST':
        flash(f'Successfully Logged in!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('signin.html')


@app.route("/Home")
def home() :
    return render_template('index.html')

@app.route("/Report")
def rep() :
    return render_template('report.html')

@app.route("/Programm")
def prog() :
    return render_template('programm.html')

@app.route("/Community")
def comm() :
    return render_template('community.html')

@app.route("/Notification")
def notify() :
    return render_template('notification.html')



if __name__ == '__main__':
    app.run(port=3000, debug=True)