import sqlite3

conn = sqlite3.connect('links.db')
c = conn.cursor()

def delete_all(tableName):
	c.execute('DELETE FROM '+tableName)
	conn.commit()

#
delete_all("stack")
delete_all("visited")

#
c.close()
conn.close()
