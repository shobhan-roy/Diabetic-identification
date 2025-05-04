from flask import Flask, render_template, request
import joblib
app= Flask(__name__)
@app.route('/')
def base():
    return render_template('home.html')
@app.route('/predict')
def predict():
    preg= request.form.get('preg')
    plas= request.form.get('plas')
    pres= request.form.get('pres')
    skin= request.form.get('skin')
    test= request.form.get('test')
    mass= request.form.get('mass')
    pedi= request.form.get('pedi')
    age= request.form.get('age')

    print(pres, plas, pres, skin, test, mass, pedi, age)
    model= joblib.load("diabetic_80.pkl")
    output= model.predict([[preg, plas, pres, skin, test, mass, pedi, age ]])

    if output[0]==0:
        print('The person is not diabetic')
    else:
        print('The person is diabetic')

    return render_template('output.html', data = data)
if __name__ == "__main__":
    app.run(debug=True)