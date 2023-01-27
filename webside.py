from flask import Flask
import data_process

data_path = '專車統計test.xlsx'

app = Flask(__name__)

@app.route("/")
def home():
    return "test"
@app.route("/login")
def login():
    return "輸入乘車資料"

if __name__ == '__main__':
    # app.run()
    data_path = '專車統計test.xlsx'
    ID, _, _ = data_process.data_trans(data_path)
    print(ID)