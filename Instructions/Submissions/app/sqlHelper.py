from sqlalchemy import create_engine
import pandas as pd
import numpy as np

class SQLHelper():

    def __init__(self):
        self.connection_string = f"sqlite:///data\hawaii.sqlite"
        self.engine = create_engine(self.connection_string)

    def get_test_precepitation(self):
        query = """
                SELECT
                     date, prcp
                FROM 
                    measurement
                WHERE date >= "2016-08-01"
                limit 100
                """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_station(self):
        query = """
              
            SELECT
                *
            FROM 
                station
            limit 50        
                """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_tobss_userQuery(self):
        query = """
              
            SELECT
                *
            FROM 
                station
            limit 50        
                """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df


    
    def get_tobs_userQuery(self, start, end):
        if(start is None and end is None):
            query = f"""
                    SELECT
                        date, tobs
                    FROM 
                        measurement                                 
                    limit 100
                    """
        elif(end is None):
            query = f"""
                    SELECT
                        date, tobs
                    FROM 
                        measurement
                    WHERE date >= '{start}'     
                    limit 100
                    """
        else:
            query = f"""
                    SELECT
                        date, tobs
                    FROM 
                        measurement
                    WHERE date >= '{start}' and date <= '{end}'              
                    limit 100
                    """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df