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
    # Here unlike q11 we use a left join between order_shoe and shoe.
    # Therefore what will happen is that the shoes that have never been ordered with have a NULL order_id.
    # so we can select only them with a where
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
