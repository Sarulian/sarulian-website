from flask import Flask, render_template
import buzzfeedshopper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipe/<buzzfeedlink>')
def recipe(buzzfeedlink):
	return 'Creating list for %s' % buzzfeedlink


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
