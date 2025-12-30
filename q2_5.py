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
    # table for countries we operate in.
    # just need id and name.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS country (
        country_id INT,
        country_name VARCHAR(63) NOT NULL,
        PRIMARY KEY (country_id)
    )
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
