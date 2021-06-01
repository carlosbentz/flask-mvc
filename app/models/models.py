import psycopg2


class ConnectionHelper():
    @staticmethod
    def get_conn_cur():
        conn = psycopg2.connect(host="localhost", database="kenzieserie", user="bentz", password="123")
        cur = conn.cursor()

        return (conn, cur)

    @staticmethod
    def close_conn_cur(conn, cur):
        conn.commit()
        cur.close()
        conn.close()


class SerieToCreate():

    def __init__(self, serie_info):
        self.serie = serie_info["serie"].title()
        self.seasons = serie_info["seasons"]
        self.released_date = serie_info["released_date"]
        self.genre = serie_info["genre"].title()
        self.imdb_rating = serie_info["imdb_rating"]
