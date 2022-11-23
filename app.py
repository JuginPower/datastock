from flask import Flask, request


app = Flask(__name__)


@app.get("/indiz")
def ask_data():
    from model import Indiz
    indiz_object = Indiz()
    return indiz_object.extract_json(), 201


@app.route("/price", methods=('GET', 'POST'))
@app.route("/price/<int:id>", methods=('GET', 'POST'))
def price(id=None):
    from model import Price
    if request.method == 'POST':
        if request.is_json:
            price_request = request.get_json()
            for item in price_request['item']:
                price_object = Price(item['id'])
                price_object + item['price']
            return price_request, 201
        return {"error": "Request must be JSON"}, 415

    elif request.method == 'GET':
        price_object = Price(id)
        return {'Datum': price_object.get_dates(), 'Preis': price_object.get_closes()}, 201


if __name__ == '__main__':
    app.run(host='0.0.0.0')
