from flask import Flask
from flask import request
import pymysql
from api.mysql_api import sql
from flask import jsonify
app = Flask(__name__)


@app.route('/api/phone')
def index():
    name = request.args.get('nickname')
    phone = sql.SelectPhone(name)
    phone = list(phone[0])
    phone = str(phone[0])
    print(phone)
    return jsonify(phone)

@app.route('/api/addkc')
def addkc():
    name = request.args.get('name')
    kecheng = request.args.get('ke')
    phone = request.args.get('phone')
    sql.insert_file_recs('ims_ypuk_tchk_kecheng',name,kecheng,phone)
    return 'ok'

@app.route('/api/getname')
def getname():
    name = request.args.get('name')
    getna = sql.getname(name)
    return getna
    # 1:scratch
    # 2:arduino
    # 3:科学课    


if __name__ == "__main__":
    app.run(debug=True)