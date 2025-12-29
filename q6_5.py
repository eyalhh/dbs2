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
    # updating uk size for european size 43.
    # converting us size 11 to uk size 9.
    cursor.execute("""
    UPDATE size
    SET uk_number = 9
    WHERE european_number = 43 AND us_number = 11
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
