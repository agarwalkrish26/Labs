from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    operator = request.args.get('operator', 'add')

    if operator == 'add':
        result = f"{a} add {b} = {a+b}"
    elif operator == 'subtract':
        result = f"{a} subtract {b} = {a-b}"
    elif operator == 'multiply':
        result = f"{a} multiply {b} = {a*b}"
    elif operator == 'divide':
        if b == 0:
            result = "Division by zero is not allowed!"
        else:
            result = f"{a} divide {b} = {a/b}"
    else:
        result = "Invalid operator!"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)