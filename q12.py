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
    # finding shoes that never got ordered.
    # checking for unsold inventory items.
    cursor.execute("""
    SELECT DISTINCT s.shoe_name
    FROM shoe s
    LEFT JOIN order_shoe os ON s.shoe_id = os.shoe_id
    WHERE os.order_id IS NULL
    ORDER BY s.shoe_name ASC
    """)
    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
