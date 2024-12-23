from order_db import order_cluster
from warehouse_db import warehouse_db_cluster
import json

def get_collection(cluster, bucket, scope, collection):
    return (
        cluster
        .bucket(bucket)
        .scope(scope)
        .collection(collection)
    )

# order from `order`.`poc`.`data`
order_id = "1"
order_collection = get_collection(order_cluster, "order", "poc", "data")
order = order_collection.get(order_id).content_as[dict]

# airline from `travel-sample`.`inventory`.`airline`
color_id = "000007e9-46af-49f0-b3ef-38ec5f9e697f"
color_collection = get_collection(warehouse_db_cluster, "vector-sample", "color", "data")
color = color_collection.get(color_id).content_as[dict]


# compose doc
doc = {
    "order": order,
    "color": {
        "color": color["color"],
        "description": color["description"]
    }
}

print(json.dumps(doc, indent=4, ensure_ascii=False))