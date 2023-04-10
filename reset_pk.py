from datalayer import Datamanager


dm = Datamanager()
indiz_price = dm.select("select indiz_id, price, zeit from indiz_price")
affected = dm.query("truncate indiz_price")
affected = dm.query("insert into indiz_price (indiz_id, price, zeit) values (%s, %s, %s);", indiz_price)
