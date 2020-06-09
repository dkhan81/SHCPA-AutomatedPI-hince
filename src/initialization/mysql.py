import mysql.connector
from ..config.access import DB_ACCESS_INFO

mysqlInstance = mysql.connector.connect(**DB_ACCESS_INFO, autocommit=True)
