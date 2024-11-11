import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(r'C://Users//haida//Desktop//local_repo//bohdan_qa_auto23//' + r'become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connection successfull. Data version is : {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def send_pachkage(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name='{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_sugar_info(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} where id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_sugar_product(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record =self.cursor.fetchall()
        return record
    
    def insert_info(self, product_id, name, description, quantity):
        query = f"INSERT OR REPLACE INTO products(id,name,description,quantity) VALUES({product_id},'{name}','{description}',{quantity})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product(self, product_id):
        query = f"DELETE from products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_info(self):
        query = f"SELECT orders.id, customers.name, products.name, products.description, orders.order_date FROM orders JOIN customers ON orders.customer_id = customers.id JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record