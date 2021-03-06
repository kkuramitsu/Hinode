from flask import Flask, render_template
app = Flask(__name__, template_folder='front/dist')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/<path:d>')
def dist(d):
	return render_template(d)


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8080)
