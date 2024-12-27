
import psycopg2
import psycopg2.extras


from database.database_constants import DBNAME, HOST, PASSWORD, PORT, USER


cursor_factory = psycopg2.extras.RealDictCursor


def base_connect():
    return psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME,
    )


def execute_query(query, param={}, fetch_one=False):
    with base_connect() as con:
        with con.cursor(cursor_factory=cursor_factory) as cur:
            cur.execute(query, param)
            con.commit()
            if fetch_one:
                return cur.fetchone()
            else:
                if cur.pgresult_ptr is not None:
                    return cur.fetchall()


def execute_query_many(query_list=[]):
    with base_connect() as con:
        with con.cursor(cursor_factory=cursor_factory) as cur:
            for query, param in query_list:
                cur.execute(query, param)
            if cur.pgresult_ptr is not None:
                return cur.fetchall()
    return []
