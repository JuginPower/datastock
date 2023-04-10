from datetime import datetime
from datalayer import Datamanager


class Price(Datamanager):

    def __init__(self, indiz_id):
        super().__init__()
        self.fk_id = indiz_id

    def get_dates(self, amount=None):
        if amount:
            return [row[0] for row in self.select(f"SELECT zeit FROM indiz_price WHERE indiz_id={self.fk_id} ORDER BY id DESC limit {amount}")]
        else:
            return [row[0] for row in self.select(f"SELECT zeit FROM indiz_price WHERE indiz_id={self.fk_id}")]

    def get_closes(self, amount=None):
        if amount:
            return [row[0] for row in self.select(f"SELECT price FROM indiz_price WHERE indiz_id={self.fk_id} ORDER BY id DESC limit {amount}")]
        else:
            return [row[0] for row in self.select(f"SELECT price FROM indiz_price WHERE indiz_id={self.fk_id}")]

    def __add__(self, other):
        orig_float = self.select("SELECT price FROM `indiz_price` ORDER BY id DESC LIMIT 1;")[0][0]

        if other == orig_float:
            return 0
        else:
            rows_affected = self.query(f"INSERT INTO indiz_price (indiz_id, price, zeit) VALUES (%s, %s, %s)",
                                       (self.fk_id, other, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            return rows_affected
