import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta

# Database connection parameters
oltp_params = {
    "dbname": "oltp_db",
    "user": "postgres",
    "password": "Luffy10$",
    "host": "localhost",
    "port": "5432"
}

olap_params = {
    "dbname": "olap_db",
    "user": "postgres",
    "password": "Luffy10$",
    "host": "localhost",
    "port": "5432"
}

def connect_to_db(params):
    return psycopg2.connect(**params)

def etl_customers(oltp_cur, olap_cur):
    oltp_cur.execute("SELECT customer_id, name, email, created_at FROM customers")
    for row in oltp_cur.fetchall():
        olap_cur.execute("""
            INSERT INTO dim_customer (customer_id, name, email, created_at)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (customer_id) DO UPDATE
            SET name = EXCLUDED.name, email = EXCLUDED.email, created_at = EXCLUDED.created_at
        """, row)

def etl_products(oltp_cur, olap_cur):
    oltp_cur.execute("SELECT product_id, name, price FROM products")
    for row in oltp_cur.fetchall():
        olap_cur.execute("""
            INSERT INTO dim_product (product_id, name, price)
            VALUES (%s, %s, %s)
            ON CONFLICT (product_id) DO UPDATE
            SET name = EXCLUDED.name, price = EXCLUDED.price
        """, row)

def etl_dates(olap_cur):
    # Generate dates for the last 5 years
    start_date = datetime.now().date() - timedelta(days=5*365)
    end_date = datetime.now().date()
    current_date = start_date
    while current_date <= end_date:
        olap_cur.execute("""
            INSERT INTO dim_date (date, day, month, year, quarter)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING
        """, (current_date, current_date.day, current_date.month, current_date.year, (current_date.month-1)//3 + 1))
        current_date += timedelta(days=1)

def etl_sales(oltp_cur, olap_cur):
    oltp_cur.execute("""
        SELECT o.order_id, o.customer_id, oi.product_id, o.order_date, oi.quantity, oi.price * oi.quantity as total_amount
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
    """)
    for row in oltp_cur.fetchall():
        order_id, customer_id, product_id, order_date, quantity, total_amount = row
        olap_cur.execute("SELECT customer_key FROM dim_customer WHERE customer_id = %s", (customer_id,))
        customer_key = olap_cur.fetchone()[0]
        olap_cur.execute("SELECT product_key FROM dim_product WHERE product_id = %s", (product_id,))
        product_key = olap_cur.fetchone()[0]
        olap_cur.execute("SELECT date_key FROM dim_date WHERE date = %s", (order_date.date(),))
        date_key_result = olap_cur.fetchone()
        if date_key_result:
            date_key = date_key_result[0]
            olap_cur.execute("""
                INSERT INTO fact_sales (order_id, customer_key, product_key, date_key, quantity, total_amount)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id, customer_key, product_key, date_key) DO UPDATE
                SET quantity = EXCLUDED.quantity, total_amount = EXCLUDED.total_amount
            """, (order_id, customer_key, product_key, date_key, quantity, total_amount))
        else:
            print(f"Warning: No matching date found in dim_date for {order_date.date()}")

def main_etl_process():
    oltp_conn = connect_to_db(oltp_params)
    olap_conn = connect_to_db(olap_params)
    
    oltp_cur = oltp_conn.cursor()
    olap_cur = olap_conn.cursor()
    
    try:
        etl_customers(oltp_cur, olap_cur)
        etl_products(oltp_cur, olap_cur)
        etl_dates(olap_cur)
        etl_sales(oltp_cur, olap_cur)
        
        olap_conn.commit()
        print("ETL process completed successfully.")
    except Exception as e:
        olap_conn.rollback()
        print(f"An error occurred during ETL: {e}")
    finally:
        oltp_cur.close()
        olap_cur.close()
        oltp_conn.close()
        olap_conn.close()

if __name__ == "__main__":
    main_etl_process()