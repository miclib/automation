import psycopg2

#Connect to postgres 
#-----------------------------
# Note: Change print to log displays 

print ("Attempting to connect PostgreSQL")
cnt = 1
# Connect to your postgres DB
conn = psycopg2.connect(dbname="car_portal" ,user="postgres", password="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM car_portal_app.car")

# Retrieve query results
for record in cur:
    record = cur.fetchone()
    print(record)
    cnt = cnt + 1



#print(records)

print ("number or records")
print(cnt)
conn.close 


