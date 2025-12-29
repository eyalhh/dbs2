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
    # updating uk size for specific european size.
    # setting uk size 5 for european 38 and us 6.
    cursor.execute("""
    UPDATE size
    SET uk_number = 5
    WHERE european_number = 38 AND us_number = 6
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
