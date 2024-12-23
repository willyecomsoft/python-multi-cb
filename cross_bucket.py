from order_db import order_cluster
import json

def get_collection(bucket, scope, collection):
    return (
        order_cluster
        .bucket(bucket)
        .scope(scope)
        .collection(collection)
    )

# order from `order`.`poc`.`data`
order_id = "1"
order_collection = get_collection("order", "poc", "data")
order = order_collection.get(order_id).content_as[dict]

# airline from `travel-sample`.`inventory`.`airline`
airline_id = "airline_10"
airline_collection = get_collection("travel-sample", "inventory", "airline")
airline = airline_collection.get(airline_id).content_as[dict]

# compose doc
doc = {
    "order": order,
    "airline": airline
}

print(json.dumps(doc, indent=4, ensure_ascii=False))


