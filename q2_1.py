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
    # creating table for shoes with id name and price.
    # name and price cant be null because every shoe needs them.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shoe (
        shoe_id INT PRIMARY KEY,
        shoe_name VARCHAR(31) NOT NULL,
        price SMALLINT NOT NULL
    )
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
