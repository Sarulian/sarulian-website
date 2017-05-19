from flask import Flask, render_template
import buzzfeedshopper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shopper')
def recipe():
	return render_template('shopper.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    buzzlink = request.form['buzzfeedlink']
    return "You typed in %s" % buzzfeedlink


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
