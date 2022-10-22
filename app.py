from flask import Flask, request
from datalayer import Datamanager

app = Flask(__name__)
dm = Datamanager()


@app.get("/")
def hello_data():
    result = dm.select("SELECT * from indiz_price")
    return str(result)


@app.post("/price")
def add_price():
    if request.is_json:
        price = request.get_json()
        dm.query(f"INSERT INTO indiz_price (indiz_id, price, zeit) VALUES ({price['id']}, {price['price']}, {price['timestamp']}")
        return price, 201
    return {"error": "Request must be JSON"}, 415


@app.post("/query")
def ask_data():
    if request.is_json:
        json_data = request.get_json()



if __name__ == '__main__':
    app.run(debug=True)
