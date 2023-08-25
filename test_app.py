from flask import Flask ,request,jsonify

app = Flask(__name__)

@app.route("/xyz",methods = ["POST","GET"])
def test():
    if request.method == "POST":
        data = request.json  # Get the JSON data from the request
        num1 = data.get("num1", 0)  # Get the value of "num1" from the JSON data, defaulting to 0 if not found
        num2 = data.get("num2", 0)  # Get the value of "num2" from the JSON data, defaulting to 0 if not found
        result = num1 + num2
        return jsonify({"result": result})


@app.route("/sub",methods = ["POST","GET"])
def sub():
    if request.method == "POST":
        data = request.json  # Get the JSON data from the request
        num1 = data.get("num1", 0)  # Get the value of "num1" from the JSON data, defaulting to 0 if not found
        num2 = data.get("num2", 0)  # Get the value of "num2" from the JSON data, defaulting to 0 if not found
        result = num1 - num2
        return jsonify({"result": result})

@app.route("/div",methods = ["POST","GET"])
def div():
    if request.method == "POST":
        data = request.json  # Get the JSON data from the request
        num1 = data.get("num1", 0)  # Get the value of "num1" from the JSON data, defaulting to 0 if not found
        num2 = data.get("num2", 0)  # Get the value of "num2" from the JSON data, defaulting to 0 if not found
        result = num1 / num2
        return jsonify({"result": result})
@app.route("/mul",methods = ["POST","GET"])
def mul():
    if request.method == "POST":
        data = request.json  # Get the JSON data from the request
        num1 = data.get("num1", 0)  # Get the value of "num1" from the JSON data, defaulting to 0 if not found
        num2 = data.get("num2", 0)  # Get the value of "num2" from the JSON data, defaulting to 0 if not found
        result = num1 * num2
        return jsonify({"result": result})
if __name__ == "__main__":
    app.run()

# 2
# write a function
# write a functoin to
# to fetch data from sql table via api
# fetch a data from mongoclb table