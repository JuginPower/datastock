from flask import Flask, request


app = Flask(__name__)


@app.get("/indiz")
def ask_data():
    from modelstock import Indiz
    indiz_object = Indiz()
    return str(indiz_object)


@app.post("/price")
def add_price():
    if request.is_json:
        from modelstock import Datamanager
        dm = Datamanager()
        price = request.get_json()
        dm.query(f"INSERT INTO indiz_price (indiz_id, price, zeit) VALUES ({price['id']}, {price['price']}, {price['timestamp']}")
        return price, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True)
