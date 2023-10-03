from dataextraction import *
import psycopg2 as pg2

hostname = 'localhost'
dbname = 'phonepe'
username = 'postgres'
pwd = '1234'
port_id = '5432'

connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)

database = connection.cursor()
print("successful")

def create_aggregated_transaction():
    database.execute('DROP TABLE IF EXISTS aggregated_transaction')

    database.execute('''CREATE TABLE IF NOT EXISTS aggregated_transaction(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            transaction_type   VARCHAR(255),
                                            transaction_count  INT,
                                            transaction_amount FLOAT(53))'''
                      )
    
    query = '''
                INSERT INTO aggregated_transaction (state, year, quarter, transaction_type, transaction_count, transaction_amount)
                VALUES (%s, %s, %s, %s, %s, %s)
                '''
    aggregated_transaction = aggregated_transaction_state()
    for _, row in aggregated_transaction.iterrows():
            values = tuple(row)
            database.execute(query, values)
    connection.commit()
if __name__ == '__main__':
    create_aggregated_transaction()
            
def create_aggregated_user():
    database.execute('DROP TABLE IF EXISTS aggregated_user')

    database.execute('''CREATE TABLE IF NOT EXISTS aggregated_user(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            brand             VARCHAR(255),
                                            brand_count       INT,
                                            brand_percentage  FLOAT)'''
                      )

    query = '''
                INSERT INTO aggregated_user (state, year, quarter, brand, brand_count, brand_percentage)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
    aggregated_user = aggregated_user_state()
    for _, row in aggregated_user.iterrows():
            values = tuple(row)
            database.execute(query, values)
            connection.commit()
if __name__ == '__main__':
    create_aggregated_user()

def create_map_transaction():
    database.execute('DROP TABLE IF EXISTS map_transaction')

    database.execute('''CREATE TABLE IF NOT EXISTS map_transaction(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            district          VARCHAR(255),
                                            transaction_count  INT,
                                            transaction_amount DECIMAL(20,5))'''
                      )

    query = '''
                INSERT INTO map_transaction (state, year, quarter, district, transaction_count, transaction_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
    map_transaction = map_transaction_state()
    for _, row in map_transaction.iterrows():
            values = tuple(row)
            database.execute(query, values)
            connection.commit()
if __name__ == '__main__':
    create_map_transaction()  

def create_map_user():
    database.execute('DROP TABLE IF EXISTS map_user')

    database.execute('''CREATE TABLE IF NOT EXISTS map_user(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            district          VARCHAR(255),
                                            registered_user   INT,
                                            app_opening       INT)'''
                      )

    query = '''
                INSERT INTO map_user (state, year, quarter, district, registered_user, app_opening)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
    map_user = map_user_state()
    for _, row in map_user.iterrows():
            values = tuple(row)
            database.execute(query, values)
            connection.commit()
if __name__ == '__main__':
    create_map_user()  

def create_top_transaction():
    database.execute('DROP TABLE IF EXISTS top_transaction')

    database.execute('''CREATE TABLE IF NOT EXISTS top_transaction(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            district          VARCHAR(255),
                                            transaction_count  INT,
                                            transaction_amount FLOAT(53))'''
                      )

    query = '''
                INSERT INTO top_transaction (state, year, quarter, district, transaction_count, transaction_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
    top_transaction = top_transaction_state()
    for _, row in top_transaction.iterrows():
            values = tuple(row)
            database.execute(query, values)
            connection.commit()
if __name__ == '__main__':
    create_top_transaction() 

def create_top_user():
    database.execute('DROP TABLE IF EXISTS top_user')

    database.execute('''CREATE TABLE IF NOT EXISTS top_user(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            district          VARCHAR(255),
                                            registered_user   INT)'''
                      )

    query = '''
                INSERT INTO top_user (state, year, quarter, district, registered_user)
                VALUES (%s, %s, %s, %s, %s)

                '''
    top_user = top_user_state()
    for _, row in top_user.iterrows():
            values = tuple(row)
            database.execute(query, values)
            connection.commit()
if __name__ == '__main__':
    create_top_user()

def create_top_transaction_pincode():
    database.execute('DROP TABLE IF EXISTS top_transaction_pincode')

    database.execute('''CREATE TABLE IF NOT EXISTS top_transaction_pincode(
                                            state             VARCHAR(255),
                                            pincode           INT,
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            transaction_count  INT,
                                            transaction_amount FLOAT(53))'''
                      )

    query = '''
                INSERT INTO top_transaction_pincode (state, pincode, year, quarter, transaction_count, transaction_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
    top_transaction_pincode = top_transaction_state_pincode()
    for _, row in top_transaction_pincode.iterrows():
            values = tuple(row)
            database.execute(query, values)
if __name__ == '__main__':
    create_top_transaction_pincode()

def create_top_user_pincode():
    database.execute('DROP TABLE IF EXISTS top_user_pincode')

    database.execute('''CREATE TABLE IF NOT EXISTS top_user_pincode(
                                            state             VARCHAR(255),
                                            pincode           INT,
                                            year              INT,
                                            quarter            VARCHAR(255),
                                            registered_user   INT)'''
                      )

    query = '''
                INSERT INTO top_user_pincode (state, pincode, year, quarter, registered_user)
                VALUES (%s, %s, %s, %s, %s)

                '''
    top_user_pincode = top_user_state_pincode()
    for _, row in top_user_pincode.iterrows():
            values = tuple(row)
            database.execute(query, values)
            connection.commit()
if __name__ == '__main__':
    create_top_user_pincode()