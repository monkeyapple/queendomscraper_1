import os
import psycopg2
from psycopg2.extensions import AsIs
from dotenv import load_dotenv
load_dotenv()
class DatabaseOperations_1():
    def create_table(self):
        command=(
            """
            CREATE TABLE qdscraper_1 (
                    id SERIAL PRIMARY KEY,
                    wjsn_views INTEGER,
                    wjsn_likes INTEGER,
                    kep1er_views INTEGER,
                    kep1er_likes INTEGER,
                    viviz_views INTEGER,
                    viviz_likes INTEGER,
                    hyolyn_views INTEGER,
                    hyolyn_likes INTEGER,
                    loona_views INTEGER, 
                    loona_likes INTEGER, 
                    bravegirls_views INTEGER, 
                    bravegirls_likes INTEGER, 
                    update_time TIMESTAMP NOT NULL

            )
            """)
        conn = None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()                
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                    conn.close()

    def insert_data(self,row,validCols):
        conn=None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            values=[row[column]for column in validCols]
            insert_statement='INSERT INTO qdscraper_1 (%s) VALUES %s'
            cur.execute(insert_statement, (AsIs(','.join(validCols)), tuple(values)))
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("database:")
            print(error)
        finally:
            if conn is not None:
                    conn.close()

class DatabaseOperations_2():
    def create_table(self):
        command=(
            """
            CREATE TABLE qdscraper_2 (
                    id SERIAL PRIMARY KEY,
                    wjsn_views INTEGER,
                    wjsn_likes INTEGER,
                    kep1er_views INTEGER,
                    kep1er_likes INTEGER,
                    viviz_views INTEGER,
                    viviz_likes INTEGER,
                    hyolyn_views INTEGER,
                    hyolyn_likes INTEGER,
                    loona_views INTEGER, 
                    loona_likes INTEGER, 
                    bravegirls_views INTEGER, 
                    bravegirls_likes INTEGER, 
                    update_time TIMESTAMP NOT NULL

            )
            """)
        conn = None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()                
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                    conn.close()

    def insert_data(self,row,validCols):
        conn=None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            values=[row[column]for column in validCols]
            insert_statement='INSERT INTO qdscraper_2 (%s) VALUES %s'
            cur.execute(insert_statement, (AsIs(','.join(validCols)), tuple(values)))
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("database:")
            print(error)
        finally:
            if conn is not None:
                    conn.close()
class DatabaseOperations_3_v():
    def create_table(self):
        command=(
            """
            CREATE TABLE qdscraper_vocal (
                    id SERIAL PRIMARY KEY,
                    wjsn_viviz_views INTEGER,
                    wjsn_viviz_likes INTEGER,
                    loona_kep1er_views INTEGER,
                    loona_kep1er_likes INTEGER,
                    hyolyn_bravegirls_views INTEGER,
                    hyolyn_bravegirls_likes INTEGER,
                    update_time TIMESTAMP NOT NULL
            )
            """)
        conn = None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()                
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                    conn.close()

    def insert_data(self,row,validCols):
        conn=None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            values=[row[column]for column in validCols]
            insert_statement='INSERT INTO qdscraper_vocal (%s) VALUES %s'
            cur.execute(insert_statement, (AsIs(','.join(validCols)), tuple(values)))
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("database:")
            print(error)
        finally:
            if conn is not None:
                    conn.close()
class DatabaseOperations_3_d():
    def create_table(self):
        command=(
            """
            CREATE TABLE qdscraper_dance (
                    id SERIAL PRIMARY KEY,
                    hoylyn_wjsn_views INTEGER,
                    hoylyn_wjsn_likes INTEGER,
                    bravegirls_loona_views INTEGER,
                    bravegirls_loona_likes INTEGER,
                    viviz_kep1er_views INTEGER,
                    viviz_kep1er_likes INTEGER,
                    update_time TIMESTAMP NOT NULL
            )
            """)
        conn = None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()                
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                    conn.close()

class DatabaseOperations_3_final():
    def create_table(self):
        command=(
            """
            CREATE TABLE qdscraper_3 (
                    id SERIAL PRIMARY KEY,
                    wjsn_views INTEGER,
                    wjsn_likes INTEGER,
                    kep1er_views INTEGER,
                    kep1er_likes INTEGER,
                    viviz_views INTEGER,
                    viviz_likes INTEGER,
                    hyolyn_views INTEGER,
                    hyolyn_likes INTEGER,
                    loona_views INTEGER, 
                    loona_likes INTEGER, 
                    bravegirls_views INTEGER, 
                    bravegirls_likes INTEGER, 
                    update_time TIMESTAMP NOT NULL

            )
            """)
        conn = None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()                
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                    conn.close()

    def insert_data(self,row,validCols):
        conn=None
        try:
            database_url=os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
            conn = psycopg2.connect(database_url)
            cur = conn.cursor()
            values=[row[column]for column in validCols]
            insert_statement='INSERT INTO qdscraper_3 (%s) VALUES %s'
            cur.execute(insert_statement, (AsIs(','.join(validCols)), tuple(values)))
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("database:")
            print(error)
        finally:
            if conn is not None:
                    conn.close()

if __name__=="__main__":
    # db_1=DatabaseOperations_1()
    # db_3_d=DatabaseOperations_3_d()
    db_3_final=DatabaseOperations_3_final()
    # db_1.create_table()
    # db_2.create_table()
else:
    "db module is imported"