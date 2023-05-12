from flask import Flask, request
import pandas as pd

df = pd.read_csv('./data/small-utilization.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MC ICD code services'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/agegroupcode/<value>', methods=["GET"])
def agegroupcode(value):
    print('value', value)
    filtered = df[df['age_group_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.route('/agegroupcode<value>/payer/<value2>')
def agegroupcode2(value, value2):
    filtered = df[df['age_group_code'] == value]
    filtered2 = filtered[filtered['payer'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")    

if __name__ == '__main__':
    app.run(debug=True)