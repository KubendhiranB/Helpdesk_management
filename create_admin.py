import sqlite3
from werkzeug.security import generate_password_hash

# Connect to the database
conn = sqlite3.connect('helpdesk.db')
cursor = conn.cursor()

# Create admin user
username = 'admin'
email = 'admin@helpdesk.com'
password = 'admin123'  # change if you want
hashed_password = generate_password_hash(password)

try:
    cursor.execute("INSERT INTO user (username, email, password, is_admin) VALUES (?, ?, ?, ?)",
                   (username, email, hashed_password, True))
    conn.commit()
    print("✅ Admin user created successfully!")
except Exception as e:
    print("⚠️ Error:", e)

conn.close()
