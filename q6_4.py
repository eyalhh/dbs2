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
    # updating uk size for european size 42.
    # converting us size 10 to uk size 8.
    cursor.execute("""
    UPDATE size
    SET uk_number = 8
    WHERE european_number = 42 AND us_number = 10
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
