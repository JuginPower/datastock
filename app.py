from flask import Flask, request


app = Flask(__name__)


@app.get("/indiz")
@app.get("/indiz/<int:id>")
def ask_data(id=None):
    from model import Indiz
    indiz_object = Indiz()
    if id:
        all_data = indiz_object.extract_json()
        return all_data[id], 201
    else:
        return indiz_object.extract_json(), 201


@app.post("/price")
@app.get("/price/<int:id>")
@app.get("/price/<int:id>/<int:amount>")
def price(id=None, amount=None):
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
        if amount:
            return {'Datum': price_object.get_dates(amount), 'Preis': price_object.get_closes(amount)}, 201
        else:
            return {'Datum': price_object.get_dates(), 'Preis': price_object.get_closes()}, 201


if __name__ == '__main__':
    app.run(host='0.0.0.0')
