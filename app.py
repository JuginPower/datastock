from flask import Flask, request


app = Flask(__name__)


@app.get("/indiz")
@app.get("/indiz/<int:id>")
def ask_data(id=None):
    from model import Indiz
    indiz_object = Indiz()
    all_data = indiz_object.extract_json()
    if id:
        return all_data[id], 201
    else:
        return all_data, 201


@app.post("/price")
@app.get("/price/<int:id>")
@app.get("/price/<int:id>/<datestart>/<dateend>")
def price(id=None, datestart=None, dateend=None):
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
        if id:
            price_object = Price(id)
            if datestart and dateend:
                pass
            else:
                return {'Datum': price_object.get_dates(), 'Preis': price_object.get_closes()}, 201
        else:
            return {"error": "Bad Request"}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
