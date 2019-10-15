#from run import app

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from run import app
from flask import jsonify
from logger import log,Print_log

import sys
sys.stdout = Print_log(open("logfile.txt", "a"), sys.stdout)
sys.stderr= sys.stdout

@app.route('/')
def index():
    return jsonify({'message':'zat'})



if __name__ == '__main__':
    app.run(debug=True)