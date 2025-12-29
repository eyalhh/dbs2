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
    # inserting the shoe inventory data.
    # listing all the shoes we have in stock with their prices.
    cursor.execute("""
    INSERT INTO shoe (shoe_id, shoe_name, price) VALUES
    (1, 'Air CS 0/1', 150),
    (2, 'Yeezy Galaxy', 200),
    (3, 'UltraBoost Pro', 180),
    (4, 'Jordan Retro 5', 190),
    (5, 'Chuck Taylor All Star', 65),
    (6, 'Vans Old Skool', 60),
    (7, 'Nike Air Max 90', 120),
    (8, 'Adidas Superstar', 80),
    (9, 'Puma Suede Classic', 70),
    (10, 'New Balance 574', 85)
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
