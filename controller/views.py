from run import app
from flask import jsonify

@app.route('/')
def index():
    return jsonify({'message':'zat'})



if __name__ == '__main__':
    app.run(debug=True)