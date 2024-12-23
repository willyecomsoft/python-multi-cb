## cross bucket & cross cluster query

> 假設有兩個cluster, 分別為order及warehouse

### connection
.env
```
ORDER_DB_CONN_STR=localhost
ORDER_DB_USERNAME=Administrator
ORDER_DB_PASSWORD=
ORDER_DB_BUCKET=order

WAREHOUSE_DB_CONN_STR=192.168.11.151
WAREHOUSE_DB_USERNAME=Administrator
WAREHOUSE_DB_PASSWORD=
WAREHOUSE_DB_BUCKET=warehouse
```


### cross bucket
**method 1: 分別對不同的bucket query** <br>
[cross_bucket.py](/cross_bucket.py)

![cross_bucket](/static/image/cross_bucket.png)

```
def get_collection(bucket, scope, collection):
    return (
        order_cluster
        .bucket(bucket)
        .scope(scope)
        .collection(collection)
    )
```

```
order_id = "1"
order_collection = get_collection("order", "poc", "data")
order = order_collection.get(order_id).content_as[dict]

airline_id = "airline_10"
airline_collection = get_collection("travel-sample", "inventory", "airline")
airline = airline_collection.get(airline_id).content_as[dict]
```

<br>

**method 2** <br>
[cross_bucket_query.py](/cross_bucket_query.py)
```
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
```

<br>

### cross cluster
[cross_cluster.py](/cross_cluster.py)
