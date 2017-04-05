from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey cutie pie'

@app.route('/rachael')
def rachael():
    return 'I love you!'

@app.route('/daisy')
def cakes():
    return 'I love you more ;)'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')