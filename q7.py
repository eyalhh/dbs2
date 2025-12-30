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
    # calculating total revenue per customer.
    # the main idea here is that we will create a table which will look like:
    # customer_id, first_name, last_name, total_amout_spent
    # where total_amount_spent is the amount of money the customer spent in total.
    # We can do this by first taking all customers, joining then with the customers that actually ordered
    # so that now we have a table with order IDs and all customers, we join this with the order_shoe
    # so that now in our table we have shoe_ids as well. Finally we connect this with the shoes table
    # to also get the price of a shoe ordered. Now we have rows in the format:
    # first name, last name, customer id, shoe id, shoe price [and some more] and now we can sum
    # the price of shoes per customer.
    cursor.execute("""
    SELECT 
        c.first_name,
        c.last_name,
        COALESCE(SUM(s.price), 0) AS total_amount_spent
    FROM customer c
    LEFT JOIN order_customer oc ON c.customer_id = oc.customer_id
    LEFT JOIN order_shoe os ON oc.order_id = os.order_id
    LEFT JOIN shoe s ON os.shoe_id = s.shoe_id
    GROUP BY c.customer_id, c.first_name, c.last_name
    ORDER BY total_amount_spent DESC
    """)
    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
