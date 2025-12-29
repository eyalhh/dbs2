import mysql.connector

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        # database is not specified here because we are creating it
        port="3307",
    )
    cursor = mydb.cursor()
    # creating the main database for the store, biu_shoes.
    # checking if it exists first so we dont get error.
    cursor.execute("""
    CREATE DATABASE IF NOT EXISTS biu_shoes
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
