from flask import Flask,  request
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

@app.route('/submit', methods=['POST'])
def submit():
    # print("ok submitted ")
    form_data = dict(request.form) 
    result = collection.insert_one(form_data)
    form_data["_id"] = str(result.inserted_id) 
    return form_data

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']
    data = {
        'data': data
    }
    return data


@app.route('/deleted')
def delete():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']
    data = {
        'data': data
    }
    return data

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=8000, debug=True)

