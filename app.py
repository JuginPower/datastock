from flask import Flask, request


app = Flask(__name__)


@app.get("/indiz")
def ask_data():
    from model import Indiz
    indiz_object = Indiz()
    return indiz_object.extract_json(), 201


@app.post("/price")
def add_price():
    if request.is_json:
        from model import Datamanager
        dm = Datamanager()
        price = request.get_json()
        dm.query(f"INSERT INTO indiz_price (indiz_id, price, zeit) VALUES ({price['id']}, {price['price']}, {price['timestamp']}")
        return price, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True)
