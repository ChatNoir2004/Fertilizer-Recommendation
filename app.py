from flask import Flask, render_template, request
import pickle
import pandas as pd

model = pickle.load(open('classifier1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve and convert input data
        Nitrogen = float(request.form.get('Nitrogen', 0))
        Potassium = float(request.form.get('Potassium', 0))
        Phosphorous = float(request.form.get('Phosphorous', 0))

        # Create a DataFrame with the same columns as used during model training
        input_data = pd.DataFrame([[Nitrogen, Potassium, Phosphorous]],
                                  columns=['Nitrogen', 'Potassium', 'Phosphorous'])

        # Predict
        result = model.predict(input_data)[0]

        # Map result to the corresponding recommendation
        if result == 0:
            result = 'TEN-TWENTY SIX-TWENTY SIX'
        elif result == 1:
            result = 'Fourteen-Thirty Five-Fourteen'
        elif result == 2:
            result = 'Seventeen-Seventeen-Seventeen'
        elif result == 3:
            result = 'TWENTY-TWENTY'
        elif result == 4:
            result = 'TWENTY EIGHT-TWENTY EIGHT'
        elif result == 5:
            result = 'DAP'
        else:
            result = 'UREA'

    except Exception as e:
        # Handle any errors
        result = f"Error: {str(e)}"

    return render_template('index.html', result=str(result))


if __name__ == '__main__':
    app.run(debug=True)
