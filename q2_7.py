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
    # customer details table with check for id length.
    # id must be exactly 9 chars or it wont accept.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer (
        customer_id VARCHAR(15),
        first_name VARCHAR(31) NOT NULL,
        last_name VARCHAR(31) NOT NULL,
        email VARCHAR(255) NOT NULL,
        city_id INT NOT NULL,
        PRIMARY KEY (customer_id),
        UNIQUE (email),
        FOREIGN KEY (city_id) REFERENCES city(city_id),
        CHECK (LENGTH(customer_id) = 9)
    )
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
