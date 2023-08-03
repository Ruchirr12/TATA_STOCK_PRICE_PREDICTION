from flask import Flask, render_template, request
import pickle



model = pickle.load(open('gradient_boosting_regressor.pkl','rb'))

app = Flask(__name__) #template folder

@app.route('/')
def stock():
    return render_template('stock.html')

@app.route('/',methods=['GET','POST'])
def predict_value():
    if request.method == 'POST':
        Open = float(request.form.get('Open'))
        High = float(request.form.get('High'))
        Low = float(request.form.get('Low'))
        Adj_Close = float(request.form.get('Adj Close'))
        Volume = float(request.form.get('Volume'))


    Prediction  = model.predict([[Open,High, Low, Adj_Close , Volume]])
    output = round( Prediction [0],2)

    return render_template('stock.html', Prediction_text='Predict Stock Price:{}'.format(output))
    
if __name__ == "__main__":
    app.run(debug=True)