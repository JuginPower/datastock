from model.datalayer import Datamanager


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
