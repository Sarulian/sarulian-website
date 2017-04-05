from flask import Flask, render_template

app = Flask(__name__)

@app.route('/rachael')
def rachael():
    return 'I love you!'

@app.route('/daisy')
def cakes():
    return 'I love you more ;)'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
