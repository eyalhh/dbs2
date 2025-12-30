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
    # table for special releases, upcoming sneakers.
    # linking to shoe table so we know which model it is.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS upcoming (
        special_id INT,
        collection_name VARCHAR(31),
        release_date DATETIME,
        shoe_id INT NOT NULL,
        PRIMARY KEY (special_id),
        FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id)
    )
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
