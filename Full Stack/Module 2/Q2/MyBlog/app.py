from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Now do something with the data (e.g., send an email, store in a database, etc.)
    return "Thank you for your message!"

if __name__ == '__main__':
    app.run(debug=True)
