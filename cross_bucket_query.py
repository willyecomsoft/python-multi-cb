from order_db import order_cluster
import json

query = """
    SELECT *
    FROM `order`.`poc`.`data` AS `order`
    JOIN `travel-sample`.`inventory`.`airline` AS airline
    ON meta(`order`).id = $order_id
    AND meta(airline).id = $airline_id
"""

order_id = "1"
airline_id = "airline_10"

results = order_cluster.query(
    query, order_id=order_id, airline_id=airline_id
)

datas = [r for r in results]

print(json.dumps(datas, indent=4, ensure_ascii=False))
