import psycopg2 as pg2
import pandas as pd

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


def total_transactions(year, quarter):
    query = '''
                SELECT transaction_type, sum(transaction_amount) AS transaction_amount 
                FROM aggregated_transaction 
                WHERE year = %s 
                AND quarter = %s 
                GROUP BY transaction_type
                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['transaction type','transaction amount']).reset_index(drop=True)
    df.index += 1
    return df
        
def top_state_transactions_amount(year, quarter):
    query = '''
                SELECT state, SUM(transaction_amount) AS top_states
                FROM top_transaction
                WHERE year = %s
                AND quarter = %s
                GROUP BY state 
                ORDER BY top_states DESC
                LIMIT 10;

                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['state','transaction amount']).reset_index(drop=True)
    df.index += 1
    return df
        
def top_state_transactions_count(year, quarter):
    query = '''
                SELECT state, SUM(transaction_count) AS top_states
                FROM top_transaction
                WHERE year = %s
                AND quarter = %s
                GROUP BY state 
                ORDER BY top_states DESC
                LIMIT 10;

                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['state', 'transaction count']).reset_index(drop=True)
    df.index += 1
    return df
        
def top_district_transactions_amount(year, quarter):
    query = '''
                SELECT district, SUM(transaction_amount) AS top_district_amount
                FROM map_transaction
                WHERE year = %s
                AND quarter = %s
                GROUP BY district 
                ORDER BY top_district_amount DESC
                LIMIT 10;

                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['district','transaction amount']).reset_index(drop=True)
    df.index += 1

    return df
        
def top_district_transactions_count(year, quarter):
    query = '''
                SELECT district, SUM(transaction_count) AS top_district_count
                FROM map_transaction
                WHERE year = %s
                AND quarter = %s
                GROUP BY district 
                ORDER BY top_district_count DESC
                LIMIT 10;

                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['district','transaction count']).reset_index(drop=True)
    df.index += 1

    return df
        
def top_pincode_transactions_amount(year, quarter):
    query = '''
                SELECT pincode, SUM(transaction_amount) AS top_pincode_amount
                FROM top_transaction_pincode
                WHERE year = %s
                AND quarter = %s
                GROUP BY pincode 
                ORDER BY top_pincode_amount DESC
                LIMIT 10;

                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['pincode','transaction amount']).reset_index(drop=True)
    df.index += 1
    return df
        
def top_pincode_transactions_count(year, quarter):
    query = '''
                SELECT pincode, SUM(transaction_count) AS top_pincode_count
                FROM top_transaction_pincode
                WHERE year = %s
                AND quarter = %s
                GROUP BY pincode 
                ORDER BY top_pincode_count DESC
                LIMIT 10;

                '''
    database.execute(query, (year, quarter))

    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['pincode', 'transaction count']).reset_index(drop=True)
    df.index += 1
    return df
        
        
def user_brand_count(year, quarter):
    query = '''
                SELECT brand, SUM(brand_count) AS user_count
                FROM aggregated_user
                WHERE year = %s
                AND quarter = %s
                GROUP BY brand
                ORDER BY user_count DESC
                LIMIT 10;

                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['brand','user count'])
    df.index += 1
    return df
        
def user_brand_count_state(year, quarter):
    query = '''
                SELECT state, brand, SUM(brand_count) AS state_user_count
                FROM aggregated_user
                WHERE year = %s
                AND quarter = %s
                GROUP BY state, brand
                ORDER BY state_user_count DESC
                LIMIT 10;
                
                '''
    database.execute(query, (year, quarter))

    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['state','brand', 'user count'])
    df.index += 1
    return df
        
def top_user_state(year, quarter):
    query = '''
                SELECT state, SUM(registered_user) AS user_count_state
                FROM top_user
                WHERE year = %s
                AND quarter = %s
                GROUP BY state
                ORDER BY user_count_state DESC
                LIMIT 10;
    
                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['state','user count'])
    df.index += 1
    return df
        
def top_user_district(year, quarter):
    query = '''
                SELECT district, SUM(registered_user) AS user_count_state
                FROM top_user
                WHERE year = %s
                AND quarter = %s
                GROUP BY district
                ORDER BY user_count_state DESC
                LIMIT 10;
    
                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['district','user count'])
    df.index += 1
    return df
        
def top_user_pincode(year, quarter):
    query = '''
                SELECT state, pincode, SUM(registered_user) AS user_count_pincode
                FROM top_user_pincode
                WHERE year = %s
                AND quarter = %s
                GROUP BY state, pincode
                ORDER BY user_count_pincode DESC
                LIMIT 10;
    
                '''
    database.execute(query, (year, quarter))
    result = database.fetchall()

    database.close()
    connection.close()

    df = pd.DataFrame(result, columns=['state','pincode','user count'])
    df.index += 1
    return df
 