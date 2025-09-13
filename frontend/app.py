from flask import Flask, render_template, request
import requests

BACKEND_URL = "http://127.0.0.1:8000"

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", name="vikas 😎 ")

@app.route("/submit", methods=["POST"])
def submit():
	form_data = dict(request.form)
	requests.post(BACKEND_URL + '/submit', data=form_data)
	return "Form submitted successfully!"

@app.route("/get_data")
def get_data():
	response = requests.get(BACKEND_URL + '/view')
	data = response.json()
	return data

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=8500, debug=True)

