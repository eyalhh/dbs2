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
    # selecting from the sales view.
    # showing the sales summary ordered by revenue.
    cursor.execute("""
    SELECT *
    FROM total_sales_per_shoe
    ORDER BY total_revenue DESC
    """)
    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
