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
    # counting available sizes for each shoe.
    # listing all shoes and how many sizes they have in stock.
    cursor.execute("""
    SELECT 
        s.shoe_name,
        COUNT(ss.size_id) AS size_count
    FROM shoe s
    LEFT JOIN shoe_size ss ON s.shoe_id = ss.shoe_id
    GROUP BY s.shoe_id, s.shoe_name
    ORDER BY s.shoe_name ASC
    """)
    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
