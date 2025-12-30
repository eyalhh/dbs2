import mysql.connector

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307",
    )
    cursor = mydb.cursor()
    # table for company orders.
    # storing order id and when it happened.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_order (
        order_id INT,
        order_date DATETIME NOT NULL,
        PRIMARY KEY (order_id)
    )
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
