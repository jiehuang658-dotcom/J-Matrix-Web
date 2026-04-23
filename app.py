import numpy as np
from flask import Flask, request, jsonify,render_template
app=Flask(__name__)
@app.route('/')
def home():
    a=np.array([[10,20],[30,40]])
    b=np.array([[1,2],[3,4]])
    sum_result=a+b
    return render_template('index.html', result=sum_result, status="success")
if __name__ == "__main__":
    app.run(port=5555,debug=True)
