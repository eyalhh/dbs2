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
    # Here we need to use a union in order to add more rows. We create a table with name, src.
    # In the first SELECT the source is always inventory since we take only from shoe,
    # and in the second its always Upcoming Release since we take from upcoming.
    cursor.execute("""
    SELECT 
        shoe_name AS name,
        'Inventory' AS source
    FROM shoe
    UNION
    SELECT 
        collection_name AS name,
        'Upcoming Release' AS source
    FROM upcoming
    WHERE collection_name IS NOT NULL
    ORDER BY source ASC, name ASC
    """)
    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
