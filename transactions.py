import psycopg2 as pg2
import pandas as pd
from SQLdata import *

hostname = 'localhost'
dbname = 'phonepe'
username = 'postgres'
pwd = '1234'
port_id = '5432'

print("successful")

def transactions(year, quarter):
    '''
    Added DB connections in the function scope
    '''
    connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)
    database = connection.cursor()
    query = '''
                SELECT 
                    SUM(map_transaction.transaction_count) AS total_transaction_count,
                    SUM(map_transaction.transaction_amount) AS total_transaction_amount,
                    AVG(map_transaction.transaction_amount/map_transaction.transaction_count) AS average_transaction_amount
                FROM
                    map_transaction
                WHERE
                    map_transaction.year = %s
                    AND map_transaction.quarter = %s
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['All PhonePe transactions', 
                                           'Total payment value', 
                                           'Avg. transaction value']).reset_index(drop=True)
        df.index += 1
        return df
    except pg2.InterfaceError as e:
        print(e)
        

def transactions_categories(year, quarter):
    connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)
    database = connection.cursor()

    query = '''
                SELECT
                SUM(CASE WHEN transaction_type = 'recharge & bill payments' THEN transaction_count ELSE 0 END) AS recharge_bill_payments,
                SUM(CASE WHEN transaction_type = 'peertopeer payments' THEN transaction_count ELSE 0 END) AS peertopeer_payments,
                SUM(CASE WHEN transaction_type = 'merchant payments' THEN transaction_count ELSE 0 END) AS merchan_payments,
                SUM(CASE WHEN transaction_type = 'financial services' THEN transaction_count ELSE 0 END) AS financial_services,
                SUM(CASE WHEN transaction_type = 'others' THEN transaction_count ELSE 0 END) AS others
                FROM
                aggregated_transaction
                WHERE
                transaction_type IN ('recharge & bill payments', 'peertopeer payments', 'merchant payments', 'financial services', 'others')
                AND year = %s
                AND quarter = %s;
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()
        

        df = pd.DataFrame(result, columns=['Recharge & bill payments', 
                                           'Peer-to-peer payments', 
                                           'Merchant payments',
                                           'Financial Services',
                                           'Others']).reset_index(drop=True)
        df.index += 1
        return df
    except pg2.InterfaceError as e:
        print(e)

def transactions_top_state(year, quarter):
    connection = pg2.connect(
            host= hostname,
            database= dbname,
            user= username,
            password= pwd,
            port= port_id)
    database = connection.cursor()
    
    query = '''
                SELECT state, SUM(transaction_count) AS total_transaction_count
                FROM aggregated_transaction
                WHERE year = %s
                AND quarter = %s
                GROUP BY state
                ORDER BY total_transaction_count DESC
                LIMIT 10;
                
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['State','Total transaction count']).reset_index(drop=True)
        df.index += 1
        return df
    
    except pg2.InterfaceError as e:
        print(e)

def transactions_top_district(year, quarter):
    connection = pg2.connect(
        host= hostname,
        database= dbname,
        user= username,
        password= pwd,
        port= port_id)
    database = connection.cursor()

    query = '''
                SELECT district, SUM(transaction_count) AS total_transaction_count
                FROM top_transaction
                WHERE year = %s 
                AND quarter = %s
                GROUP BY district
                ORDER BY total_transaction_count DESC
                LIMIT 10;
                
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['District','Total transaction count']).reset_index(drop=True)
        df.index += 1
        return df
    
    except pg2.InterfaceError as e:
        print(e)

def transactions_top_pincode(year, quarter):
    connection = pg2.connect(
        host= hostname,
        database= dbname,
        user= username,
        password= pwd,
        port= port_id)
    database = connection.cursor()

    query = '''
                SELECT pincode , SUM(transaction_count) AS total_transaction_count
                FROM top_transaction_pincode
                WHERE year = %s 
                AND quarter = %s
                GROUP BY pincode
                ORDER BY total_transaction_count DESC
                LIMIT 10;
                
                '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()
  
        df = pd.DataFrame(result, columns=['Pincode','Total transaction count']).reset_index(drop=True)
        df.index += 1
        return df
    
    except pg2.InterfaceError as e:
        print(e)

def geo_transactions(year, quarter):
    connection = pg2.connect(
        host= hostname,
        database= dbname,
        user= username,
        password= pwd,
        port= port_id)
    database = connection.cursor()

    query = '''
                SELECT * FROM aggregated_transaction
                WHERE year = %s
                AND quarter = %s

        '''
    try:
        database.execute(query,(year, quarter))
        result = database.fetchall()
        if not result:
            print('No results')
        database.close()
        connection.close()

        df = pd.DataFrame(result, columns=['state',
                                            'year',
                                            'quarter',
                                            'transaction_type',
                                            'transaction_count',
                                            'transaction_amount']).reset_index(drop=True)
        df.index += 1
        return df

    except pg2.InterfaceError as e:
        print(e)

#if __name__ == '__main__':
#    print(transactions('2018','q1'))