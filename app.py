from flask import Flask, request


app = Flask(__name__)


"""@app.get("/indiz")
@app.get("/indiz/<int:id>")
def ask_data(id=None):
    from model import Indiz
    indiz_object = Indiz()
    all_data = indiz_object.extract_json()
    if id:
        return all_data[id], 201
    else:
        return all_data, 201"""

@app.get("/name")
@app.get("/name/<int:id>")
def ask_name(id=None):
    from model import Indiz
    indiz_object = Indiz()
    if id:
        return indiz_object.get_one_name(id), 201
    elif not id:
        return indiz_object.get_names(), 201


@app.get("/id")
@app.get("/id/<name>")
def ask_id(name=None):
    from model import Indiz
    indiz_object = Indiz()
    if name:
        return str(indiz_object.get_one_id(name)), 201
    elif not name:
        return indiz_object.get_ids(), 201


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
        if id:
            price_object = Price(id)
            if amount:
                return {'Datum': price_object.get_dates(amount), 'Preis': price_object.get_closes(amount)}, 201    
            return {'Datum': price_object.get_dates(), 'Preis': price_object.get_closes()}, 201
        return {"error": "Bad Request"}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
