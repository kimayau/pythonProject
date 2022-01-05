import sqlite3

conn = sqlite3.connect('stock.db')

c = conn.cursor()

# c.execute("""CREATE TABLE stock_tickers (
#             Symbol text,
#             Last_scale real,
#             Market_cap integer,
#            Country text
#           )""")
# c.execute("INSERT INTO stock_tickers VALUES('AA','Alcoa corporation common stock',53.11,-1.15,9937048137,'NaN')")

with open('updated_stock_tickers.csv','r') as file:
    for row in file:
        c.execute("INSERT INTO stock_tickers VALUES (?,?,?,?,?,?)",row.split(","))
        conn.commit()


print('\n,Record Transfered succesfully')

c.execute("SELECT * FROM stock_tickers")

print(c.fetchmany(5))
conn.commit()

conn.close()

