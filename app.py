from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/css.html')
def css():
    return render_template('css.html')

@app.route('/dummy.html')
def dummy():
    return render_template('dummy.html')

@app.route('/boxes.html')
def boxes():
	return render_template('boxes.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
