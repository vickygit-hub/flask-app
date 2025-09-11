from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv('uri')


# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.test

collection = db['flask-tutorial']
    


app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", name="vikas 😎 ")

app.route('/submit', methods=['post'])
def submit():
      form_data = dict(request.form)
      collection.insert_one(form_data)
      return form_data

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=6000, debug=True)

