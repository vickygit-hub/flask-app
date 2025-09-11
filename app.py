from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello, flask basic app setup is ready"

@app.route("/api")
def name():
    # get values from query string ?name=Vicky&age=20&mobile=12345
    name = request.values.get('name')
    age = request.values.get('age')
    mobile = request.values.get('mobile')

    # handle missing values safely
    if not name or not age or not mobile:
        return "Error: please provide name, age, and mobile in query string."

    age = int(age)
    mobile = int(mobile)

    if age > 18:
        return f"Welcome to site, {name}! Your mobile is {mobile}"
    else:
        return f"Sorry {name}, not eligible yet. Wait for {18 - age} more years."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
