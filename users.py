import psycopg2 as pg2
import pandas as pd

hostname = 'localhost'
dbname = 'phonepe'
username = 'postgres'
pwd = '1234'
port_id = '5432'


print("successful")

def users(year, quarter):
    connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)

    database = connection.cursor()
    query = '''
                SELECT 
                SUM(registered_user) as total_user_count,
                SUM(app_opening) as total_appopening_count
                FROM map_user
                WHERE year = %s
                AND quarter = %s;
                
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['Registered PhonePe users','PhonePe app opens']).reset_index(drop=True)
        df.index += 1
        return df
    except pg2.InterfaceError as e:
        print(e)

def users_top_state(year, quarter):
    connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)
    database = connection.cursor()
    
    query = '''
                SELECT
                state,
                SUM(registered_user) AS total_registered_users
                FROM map_user
                WHERE year = %s
                AND quarter = %s
                GROUP BY state
                ORDER BY total_registered_users DESC
                LIMIT 10;
                
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['State','Total registered users']).reset_index(drop=True)
        df.index += 1
        return df
    except pg2.InterfaceError as e:
        print(e)

def users_top_district(year, quarter):
    connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)
    database = connection.cursor()
    
    query = '''
                SELECT
                district,
                SUM(registered_user) AS total_registered_users
                FROM top_user
                WHERE year = %s
                AND quarter = %s
                GROUP BY district
                ORDER BY total_registered_users DESC
                LIMIT 10;
                
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['District','Total registered users']).reset_index(drop=True)
        df.index += 1
        return df
    except pg2.InterfaceError as e:
        print(e)

def users_top_pincode(year, quarter):
    connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)
    database = connection.cursor()
    
    query = '''
                SELECT
                pincode,
                SUM(registered_user) AS total_registered_users
                FROM top_user_pincode
                WHERE year = %s
                AND quarter = %s
                GROUP BY pincode
                ORDER BY total_registered_users DESC
                LIMIT 10;
                
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['Pincode','Total registered users']).reset_index(drop=True)
        df.index += 1
        return df
    except pg2.InterfaceError as e:
        print(e)