import pymysql
#import mysql-connector-python

class Employee:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="employee"
        )
        self.cursor = self.conn.cursor()
        print("Connected")

    # CREATE
    def create_employee(self, eid, name, salary):
        self.cursor.execute(
            "INSERT INTO employe (eid, name, salary) VALUES (%s, %s, %s)",
            (eid, name, salary)
        )
        self.conn.commit()
        print("Employee created successfully")

    # READ
    def read_employees(self):
        self.cursor.execute("SELECT * FROM employe")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    # UPDATE
    def update_employee(self, emp_id, new_salary):
        self.cursor.execute(
            "UPDATE employe SET salary=%s WHERE id=%s",
            (new_salary, emp_id)
        )
        self.conn.commit()
        print("Employee updated successfully")

    # DELETE
    def delete_employee(self, emp_id):
        self.cursor.execute("DELETE FROM employe WHERE id=%s", (emp_id,))
        self.conn.commit()
        print("Employee deleted successfully")

    # Close connection
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed")


#============================================


db = Employee()

# CREATE
db.create_employee(1, "Alice", 50000)

# READ
db.read_employees()

# UPDATE
db.update_employee(1, 60000)
db.read_employees()

# DELETE
db.delete_employee(1)
db.read_employees()

# Close connection
db.close()



#============================================