from client import CouchbaseClient
from dotenv import load_dotenv
import os

load_dotenv()

order_conn_str = os.getenv("ORDER_DB_CONN_STR", 'localhost')
order_username = os.getenv("ORDER_DB_USERNAME", 'Administrator')
order_password = os.getenv("ORDER_DB_PASSWORD", 'couchbase')

order_db_client = CouchbaseClient(order_conn_str, order_username, order_password)
order_cluster = order_db_client.cluster

