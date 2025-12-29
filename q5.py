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
    # adding preorder available column to upcoming table.
    # using bit type for boolean flag, default is 0.
    cursor.execute("""
    ALTER TABLE upcoming
    ADD COLUMN pre_order_available BIT DEFAULT 0
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
