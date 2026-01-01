from flask import Flask, render_template, request
import pickle
import numpy as np

application = Flask(__name__)
app = application

# Load model & scaler
reg_model = pickle.load(open('model/reg.pkl', 'rb'))
standard_scaler = pickle.load(open('model/scaler.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        data = [
            float(request.form['Temperature']),
            float(request.form['RH']),
            float(request.form['Ws']),
            float(request.form['Rain']),
            float(request.form['FFMC']),
            float(request.form['DMC']),
            float(request.form['ISI']),
            float(request.form['Classes']),
            float(request.form['Region'])
        ]

        scaled_data = standard_scaler.transform([data])
        result = reg_model.predict(scaled_data)[0]

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)