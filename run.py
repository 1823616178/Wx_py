from flask import Flask
from flask import request
import pymysql
from api.mysql_api import sql
from flask import jsonify
from api.app import app
def main():
    app.run()


if __name__ == '__main__':
    main()

