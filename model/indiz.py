from model.datalayer import Datamanager
from model.urlmanager import Url


class Indiz(Datamanager):

    def __init__(self):
        super().__init__()
        self._names = [row[0] for row in self.select("SELECT name FROM indiz")]
        self._ids = [row[0] for row in self.select("SELECT id FROM indiz")]

    def extract_json(self):

        jsondata = {}

        for indiz_id, name in zip(self.get_ids(), self.get_names()):
            url_object = Url(indiz_id)
            url_list = url_object.get_url()
            jsondata.update({indiz_id: {'name': name, 'url': []}})

            for url in url_list:
                tag = url_object.get_tag(url)
                classname = url_object.get_classname(url)
                item = {'urlstring': url, 'tag': tag, 'classname': classname}
                jsondata[indiz_id]['url'].append(item)

        return jsondata

    def get_names(self):
        return self._names

    def get_ids(self):
        return self._ids
