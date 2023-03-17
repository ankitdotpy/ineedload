import pickle
from flask import Flask,request,render_template

model_pickle = open('./models/exports/classifier_model.pkl','rb')
model = pickle.load(model_pickle)

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/ping',methods=['GET'])
def ping():
    return {'message':'Hi there'}

@app.route('/predict',methods=['POST'])
def predict():
    # print(request.form.to_dict())
    res = request.form.to_dict()
    print(res)
    gender = int(res['gender'])
    married = int(res['married'])
    dep = 0
    edu = int(res['education'])
    emp = 1
    income = int(res['income'])
    coincome = 0
    amt = int(res['amount'])
    term = int(res['term'])
    chist = int(res['chist'])
    area = int(res['area'])
    p = model.predict([[gender,married,dep,edu,emp,income,coincome,amt,term,chist,area]])
    if p==1:
        return render_template('success.html')
    else:
        return render_template('rejected.html')
    # return "yay"
    

