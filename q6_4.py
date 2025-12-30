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
    # Set uk_number 8 for us=10 and european=42
    cursor.execute("""
    UPDATE size
    SET uk_number = 8
    WHERE european_number = 42 AND us_number = 10
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
