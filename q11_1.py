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
    # We're creating a view called total_sales_per_shoe.
    # This view returns a table with 3 columns - shoe_id, name, and the total revenue from this shoe.
    # We find the total revenue from a given shoe with a JOIN on the shoes and order_shoes
    # this creates a column where there are only shoes that have been ordered.
    # We take the sum of their prices (because it will be in the JOIN table) and put it in total_revenue
    cursor.execute("""
    CREATE OR REPLACE VIEW total_sales_per_shoe AS
    SELECT 
        s.shoe_id,
        s.shoe_name,
        SUM(s.price) AS total_revenue
    FROM shoe s
    INNER JOIN order_shoe os ON s.shoe_id = os.shoe_id
    GROUP BY s.shoe_id, s.shoe_name
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
