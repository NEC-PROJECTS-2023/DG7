from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
import transformers
from transformers import pipeline
mod=pipeline("summarization",model="facebook/bart-large-cnn")
@app.route('/')
def home():
    return render_template('front.html')
@app.route("/summarize",methods=['POST','GET'])
def predict():
    body=request.form['input1']
    result=mod(body)
    return render_template('summary.html',result=result)
if __name__== '__main__':
    app.run(debug=True)