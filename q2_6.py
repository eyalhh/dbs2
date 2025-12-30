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
    # cities table linked to countries.
    # each city must belong to a country.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS city (
        city_id INT,
        city_name VARCHAR(63) NOT NULL,
        country_id INT NOT NULL,
        PRIMARY KEY (city_id),
        FOREIGN KEY (country_id) REFERENCES country(country_id)
    )
    """)
    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
