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
        from model import Price
        price_request = request.get_json()
        for item in price_request['item']:
            price_object = Price(item['id'])
            price_object + item['price']
        return price_request, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True)
