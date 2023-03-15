from flask import Flask,render_template,request
from app.utils import predictions
import CONFIG
app=Flask(__name__)
@app.route('/')
def model():
    return render_template("iris.html")


@app.route('/predict',methods= ["POST","GET"])
def predict_species():
    data= request.form
    pred_obj= predictions()
    predicted_species=pred_obj.predicted_species(data)
    print(predicted_species)

    return str(predicted_species)


if __name__=="__main__":
    app.run(host=CONFIG.HOST_NAME,port=CONFIG.PORT_NUMBER)


