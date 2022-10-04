import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00002', 'Alex', 'Smith', 'male');""")
conn.commit()
cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)
