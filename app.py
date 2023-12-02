from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))


@app.route('/', methods=['POST', 'GET'])
def prediction():
    message = ''
    if request.method == 'POST':
        int_features=  [ np.array( [int(x) for x in request.form.values()] ) ]
        prediction=model.predict( int_features )[0]
        message = 'Your Forest is in Danger.' if prediction else 'Your Forest is safe.'

    return render_template('forest.html', prediction = message)
   

if __name__ == '__main__':
    app.run(debug=True)
