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
    # Set uk_number 9 for us=11 and european=43
    cursor.execute("""
    UPDATE size
    SET uk_number = 9
    WHERE european_number = 43 AND us_number = 11
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
