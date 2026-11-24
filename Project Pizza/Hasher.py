import sqlite3
import bcrypt

# Connect to your database file
conn = sqlite3.connect("restaurant.db")  # Replace with your actual DB filename!
cursor = conn.cursor()

# Get all current employee passwords
cursor.execute("SELECT employeeid, password FROM employee")
employees = cursor.fetchall()

for emp_id, plain_password in employees:
    # Only hash if it hasn't been hashed already (bcrypt hashes start with $2)
    if not plain_password.startswith("$2"):
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cursor.execute("UPDATE employee SET password = ? WHERE employeeid = ?", (hashed, emp_id))

conn.commit()
conn.close()

print("All existing plaintext passwords have been successfully upgraded to bcrypt hashes!")