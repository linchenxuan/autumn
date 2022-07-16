from dataclasses import dataclass
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


MYSQL_DB = "autumn_user_service"
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "LYL9121204"

DB = ReconnectMysqlDatabase(MYSQL_DB, host=MYSQL_HOST,
                            port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD)
