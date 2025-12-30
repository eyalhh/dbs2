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
    # Set uk_number 5 for us=6 and european=38
    cursor.execute("""
    UPDATE size
    SET uk_number = 5
    WHERE european_number = 38 AND us_number = 6
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
