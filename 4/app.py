from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        return jsonify(data=data)
    else:
        data = request.args.get('data', 'Hello Melinda')
        return jsonify(data=data)

@app.route('/square/<int:num>', methods=['GET'])
def square(num):
    return jsonify(square=num*num)

if __name__ == '__main__':
    app.run(debug=True)
