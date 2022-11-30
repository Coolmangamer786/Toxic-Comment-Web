from flask import Flask, render_template, request, redirect, url_for
import warnings
from test import predict

warnings.filterwarnings('ignore')


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        comment = request.form['comment']
        return render_template('result.html',ans=predict(comment))
        # return redirect(url_for('result',ans=predict(comment)))
        # return f"{output[0][1]}"
    return render_template('index.html')




if __name__ == "__main__":
    app.run()
