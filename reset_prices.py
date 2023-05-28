from datalayer import Datamanager
from datetime import datetime


prev_year = datetime.now().year-1
dm = Datamanager()
indiz_price = dm.select(f"select indiz_id, price, zeit from indiz_price where year(zeit)={prev_year}")
affected = 0

if len(indiz_price) > 0:
    affected = dm.query(f"create table indiz_price_{prev_year} as select * from indiz_price where year(zeit)={prev_year}")
    print(affected)
else:
    print(f"Time: {datetime.now()}\nDid nothing")


# Funktioniert aber ich muss noch reset pk aus der älteren Version auf die neu erstellte und alte Tabelle anwenden.
