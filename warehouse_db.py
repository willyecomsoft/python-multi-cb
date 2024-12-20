from client import CouchbaseClient
from dotenv import load_dotenv
import os

load_dotenv()

warehouse_conn_str = os.getenv("WAREHOUSE_DB_CONN_STR", 'localhost')
warehouse_username = os.getenv("WAREHOUSE_DB_USERNAME", 'Administrator')
warehouse_password = os.getenv("WAREHOUSE_DB_PASSWORD", 'couchbase')
warehouse_bucket = os.getenv("WAREHOUSE_DB_BUCKET", 'order')

warehouse_db_client = CouchbaseClient(warehouse_conn_str, warehouse_username, warehouse_password)
warehouse_db = warehouse_db_client.bucket();