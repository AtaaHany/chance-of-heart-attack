from flask import Flask, render_template, request, url_for
import pickle
import pandas as pd


#--------------------------------------------------------------------------------------

app =Flask(__name__)


#load the model
model = pickle.load(open('model\RF_clf-1.0.pkl', 'rb'))


#Read html files:

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/report', methods= ['GET', 'POST'])
def report():
    if request.method=="GET":
        return render_template('report.html')
    
    if request.method=="POST":
        age = request.form['age']
        gender = request.form['gender']
        chesspain = request.form['chesspain']
        Vessels = request.form['Vessels']
        ChessPainType = request.form['ChessPainType']
        Cholsterol = request.form['Cholsterol']
        BloodSugar = request.form['BloodSugar']
        ECG = request.form['ECG']
        HeartRate = request.form['HeartRate']
        BloodPressure = request.form['BloodPressure']
        Slop = request.form['Slop']
        Thaliunm = request.form['Thaliunm']
        #OldPeak = request.form['OldPeak']
        
        input_variables = pd.DataFrame([[age, gender, ChessPainType, BloodPressure, Cholsterol, BloodSugar, ECG, HeartRate, Vessels, Slop, chesspain, Thaliunm]],
                                    columns=['age', 'gender', 'ChessPainType', 'BloodPressure', 'Cholsterol', 'BloodSugar', 'ECG', 'HeartRate', 'Vessels', 'Slop', 'chesspain', 'Thaliunm'],
                                       dtype=str)
        i_V= input_variables.to_numpy()
        prediction = model.predict(i_V)
            
        if int(prediction) ==1:
            prediction ='High Chance !!!'
            
        else:
            prediction ='Low Chance'
            
        
        return render_template('report.html', prediction=prediction)



if __name__ == '__main__':
    app.run()

#-----------------------------------------------------------------------------------------