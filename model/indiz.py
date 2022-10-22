from datetime import datetime
from model.datalayer import Datamanager


class Indiz(Datamanager):

    def __init__(self):
        super().__init__()
        self._names = [row[0] for row in self.select("SELECT name FROM indiz")]
        self._ids = [row[0] for row in self.select("SELECT id FROM indiz")]

    def get_names(self):
        return self._names

    def get_ids(self):
        return self._ids


class Price(Datamanager):

    def __init__(self, indiz_id):
        super().__init__()
        self.fk_id = indiz_id

    def get_dates(self):

        return [row[0] for row in self.select(f"SELECT zeit FROM indiz_price WHERE indiz_id={self.fk_id}")]

    def get_closes(self):

        return [row[0] for row in self.select(f"SELECT price FROM indiz_price WHERE indiz_id={self.fk_id}")]

    def __add__(self, other):

        rows_affected = self.query(f"INSERT INTO indiz_price (indiz_id, price, zeit) VALUES (%s, %s, %s)",
                                   (self.fk_id, other, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return rows_affected


class Url(Datamanager):

    def __init__(self, indiz_id):
        super().__init__()
        self.fk_id = indiz_id
        self._url = [row[0] for row in self.select(f"SELECT url FROM indiz_url WHERE indiz_id={self.fk_id} AND active=1")]

    def get_url(self):

        return self._url

    def get_tag(self, urlname):

        return self.select(f"SELECT tag FROM indiz_url WHERE url='{urlname}'")[0][0]

    def get_classname(self, urlname):

        return self.select(f"SELECT classname FROM indiz_url WHERE url='{urlname}'")[0][0]
