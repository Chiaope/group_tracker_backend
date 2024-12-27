
import psycopg2

from database.database_constants import DBNAME, HOST, PASSWORD, PORT, USER


class DatabaseService:
    def execute_query(self, query, param={}):
        with psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME,
        ) as con:
            with con.cursor() as cur:
                cur.execute(query, param)
                results = cur.fetchall()
        return results
