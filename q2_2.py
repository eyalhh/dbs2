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
    # creating table for sizes, european and US numbers.
    # us number is optional (as assignment says).
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS size (
        size_id INT,
        european_number TINYINT NOT NULL,
        us_number TINYINT,
        PRIMARY KEY (size_id)
    )
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
