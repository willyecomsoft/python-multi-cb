from __future__ import annotations
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator


class CouchbaseClient(object):
    """Class to handle interactions with Couchbase cluster"""

    def __init__(self, conn_str: str, username: str, password: str) -> CouchbaseClient:
        self.cluster = None
        self.bucket = None
        self.scope = None
        self.conn_str = conn_str
        self.username = username
        self.password = password
        self.connect()
    
    def connect(self) -> None:
        print(f"connecting to {self.conn_str}...")
        auth = PasswordAuthenticator(self.username, self.password)
        cluster_opts = ClusterOptions(auth)
        self.cluster = Cluster(self.conn_str, cluster_opts)
        print(f"{self.conn_str} connected.")
