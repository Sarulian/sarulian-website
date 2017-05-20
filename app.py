from flask import Flask, render_template, request
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
    recipe_list = buzzfeedshopper.get_recipe_from_link(buzzlink)
    buzzfeedshopper.send_to_wunderlist(recipe_list)
    return "The recipe from %s has be added to your Wunderlist!" % buzzlink


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
