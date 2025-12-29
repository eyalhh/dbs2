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
    # finding average price per size.
    # grouping by size and calculating average price for shoes in that size.
    cursor.execute("""
    SELECT 
        sz.european_number,
        sz.us_number,
        AVG(s.price) AS average_price
    FROM size sz
    INNER JOIN shoe_size ss ON sz.size_id = ss.size_id
    INNER JOIN shoe s ON ss.shoe_id = s.shoe_id
    GROUP BY sz.size_id, sz.european_number, sz.us_number
    ORDER BY average_price DESC
    """)
    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
