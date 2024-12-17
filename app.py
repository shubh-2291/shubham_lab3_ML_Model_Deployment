from flask import Flask, render_template, request
import pickle
import numpy as np
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb')) ## rb :- read binary


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data1 = request.form['present_price']
        data2 = request.form['kms_driven']
        data3 = request.form['fuel_type']
        data4 = request.form['seller_type']
        data5 = request.form['transmission']
        data6 = request.form['owner']
        data7 = request.form['age_of_car']
        
        if not all([data1, data2, data3, data4, data5, data6, data7]):
            raise ValueError("All fields must be filled out.")
        
        arr = np.array([[data1, data2, data3, data4, data5, data6, data7]], dtype=float)
        pred = model.predict(arr)
        return render_template('predict.html', data=cleanvalue(pred))
    
    except ValueError as e:
        return render_template('400.html', error_message="Invalid input type. Please enter valid numbers."), 400

    except Exception as e:
        return render_template('500.html'), 500

def cleanvalue(val):
    val = str(val)
    return val[1:len(val)-1]

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)