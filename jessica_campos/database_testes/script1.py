
import sqlite3

conn = sqlite3.connect("funcionarios.db")

cur = conn.cursor()

#sql_command = """CREATE TABLE employee(
#    id INTENGER PRIMARY KEY,
#    first_name VARCAHR(255),
#   lasst_name VARCAHR(255),
#);"""

print("Done...")