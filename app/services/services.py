from app.models.models import ConnectionHelper, SerieToCreate


class KenzieSerieServices():

    @staticmethod
    def create_table(cur):
        cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ka_series (
            id  BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
        ); 
        """
        )


    @staticmethod
    def insert_table(data):

        try:
            serie_data = SerieToCreate(data)
        except:
            return False

        conn, cur = ConnectionHelper.get_conn_cur()
        KenzieSerieServices.create_table(cur)

        cur.execute(
        """
        INSERT INTO ka_series (serie, seasons, released_date, genre, imdb_rating)
        VALUES
            ('%s', '%s', '%s', '%s', '%s')
        RETURNING *;
        """ 
        % (
        serie_data.serie,  
        serie_data.seasons,
        serie_data.released_date,  
        serie_data.genre,  
        serie_data.imdb_rating)
        )

        created_serie = cur.fetchone()
        fieldnames = [i[0] for i in cur.description]

        created_serie = dict(zip(fieldnames, created_serie))

        ConnectionHelper.close_conn_cur(conn, cur)

        return created_serie


    @staticmethod
    def select_table():
        conn, cur = ConnectionHelper.get_conn_cur()
        KenzieSerieServices.create_table(cur)

        cur.execute(
        """
        SELECT * FROM ka_series;
        """
        )
        selected_series = cur.fetchall()
        fieldnames = [i[0] for i in cur.description]

        selected_series = [dict(zip(fieldnames, serie)) for serie in selected_series]

        ConnectionHelper.close_conn_cur(conn, cur)

        return selected_series

    
    @staticmethod
    def select_table_by_id(id):
        conn, cur = ConnectionHelper.get_conn_cur()
        KenzieSerieServices.create_table(cur)

        cur.execute(
        """
        SELECT * FROM ka_series
        WHERE
            id = '%s';
        """
        % id
        )

        fieldnames = [i[0] for i in cur.description]

        selected_serie = cur.fetchone()

        if selected_serie:
            selected_serie = dict(zip(fieldnames, selected_serie))

        ConnectionHelper.close_conn_cur(conn, cur)

        return selected_serie
