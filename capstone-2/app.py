# from flask import Flask, request, render_template
# import pandas as pd
# import numpy as np
# import pickle
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)

# # Load the trained model

# model = pickle.load(open('linearmodel.pkl', 'rb')) # Assuming you saved your trained model as 'trained_model.pkl'

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         # Get the input data from the form
#         jan = float(request.form['jan'])
#         feb = float(request.form['feb'])
#         mar = float(request.form['mar'])
#         apr = float(request.form['apr'])
#         may = float(request.form['may'])
#         jun = float(request.form['jun'])
#         jul = float(request.form['jul'])
#         aug = float(request.form['aug'])
#         sep = float(request.form['sep'])
#         oct = float(request.form['oct'])
#         nov = float(request.form['nov'])
#         dec = float(request.form['dec'])
        
#         # Prepare the input data for prediction
#         input_data = np.array([[jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]])
        
#         # Standardize the input data
#         scaler = StandardScaler()
#         input_data_scaled = scaler.fit_transform(input_data)
        
#         # Predict the annual return
#         annual_return = model.predict(input_data_scaled)
        
#         return render_template('result.html', annual_return=annual_return)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open('linearmodel.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input data from the form
        jan = float(request.form['jan'])
        feb = float(request.form['feb'])
        mar = float(request.form['mar'])
        apr = float(request.form['apr'])
        may = float(request.form['may'])
        jun = float(request.form['jun'])
        jul = float(request.form['jul'])
        aug = float(request.form['aug'])
        sep = float(request.form['sep'])
        oct = float(request.form['oct'])
        nov = float(request.form['nov'])
        dec = float(request.form['dec'])
        
        # Prepare the input data for prediction
        input_data = np.array([[jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]])
        
        # Scale the input data
        input_data_scaled = scaler.transform(input_data)
        
        # Predict the annual return
        annual_return = model.predict(input_data_scaled)
        
        return render_template('result.html', annual_return=annual_return[0])

if __name__ == '__main__':
    app.run(debug=True)

