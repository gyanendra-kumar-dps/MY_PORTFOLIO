from flask import *
import current_temp
app=Flask(__name__,static_folder='static')
@app.route('/')
def main():
    return render_template('Home.html',error=False)
@app.route('/srch',methods=["POST","GET"])
def handle():
    if len(current_temp.temp(str(request.form['inp1'])))==1:
        return redirect(url_for('main'))
    else:
        return redirect(url_for('srch',city=str(request.form['inp1'])))
@app.route('/search/<city>',methods=['POST','GET'])
def srch(city):
    data=current_temp.temp(city)
    print(data)
    return render_template('weatherWebsite.html',data=data)
@app.route('/about')
def abt():
    return render_template('About.html')
app.run(port=8770)