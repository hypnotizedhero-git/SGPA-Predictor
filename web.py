from flask import Flask,render_template,request
import pandas as pd
import numpy as nm
import webbrowser
import pickle
app= Flask(__name__)

# model=pickle.load(open('model.pkl','rb'))

@app.route("/predict",methods=["POST","GET"])
def predict():
    return render_template("index.html")

@app.route("/submit",methods=["POST","GET"])
def submit():
    name=request.form.get("id_no")
    data=pd.read_csv("final.csv")
    d=pd.read_csv("INTERNAL_EVAL.csv")
    x=data[data["ID"]==name]
    score=x['Predicted'].values
    list=score.tolist()
    y=d[d["ID"]==name]
    c1=y['CN_U1'].values
    c2=y['CN_U2'].values
    c3=y['CN_A'].values
    d1=y['DAA_U1'].values
    d2=y['DAA_U2'].values
    d3=y['DAA_A'].values
    a1=y['AI_U1'].values
    a2=y['AI_U2'].values
    a3=y['AI_A'].values
    ct=c1+c2+c3
    dt=d1+d2+d3
    at=a1+a2+a3
    cs=""
    ds=""
    ass=""
    if(ct>20):
        cs+="yay good performance in CN!!"
    elif(ct<=20 and ct>=12):
        cs+="average performance in CN!!"
    elif(ct<12):
        cs+="ohh poor performance in CN!!"
    if(dt>20):
        ds+="yay good performance in DAA!!"
    elif(dt<=20 and dt>=12):
        ds+="average performance in DAA!!"
    elif(dt<12):
        ds+="ohh poor performance in DAA!!"
    if(at>20):
        ass+="yay good performance in AI!!"
    elif(at<=20 and at>=12):
        ass+="average performance in AI!!"
    elif(at<12):
        ass+="ohh poor performance in AI!!"
    return render_template("submit.html",text=name,SGPA=list,x=ct,y=dt,z=at,a=cs,b=ds,c=ass)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/predict")
    app.run()
    