import pymongo
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/fetch", methods=["GET", "POST"])
def fetch():
    # Connect to the database
    if request.method == "POST":
        connection_string = "mongodb://localhost:27017"
        dbconn = pymongo.MongoClient(connection_string)
        db = dbconn["ecomm_data"]
        collection = db["product"]

        # Define query (None for fetching all documents)
        query = None

        # Fetch the data
        if query is None:
            documents = collection.find()
        else:
            documents = collection.find(query)

        result = [doc for doc in documents]
        dbconn.close()
        return jsonify(result)

if __name__ == "__main__":
    app.run()
