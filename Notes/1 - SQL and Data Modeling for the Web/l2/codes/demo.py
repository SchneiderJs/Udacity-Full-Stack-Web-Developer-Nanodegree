import psycopg2

# establish a connection
connection = psycopg2.connect(
    database="example", user="postgres", password="postgres", port=5432)

# a interface that allows to queue work to perform database operations
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS todos;")

cursor.execute('''
  CREATE TABLE todos (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

# 1st way of insertion
cursor.execute(
    'INSERT INTO todos (id, completed) VALUES (%s, %s);', (1, True))

# 2nd way of insertion
SQL = 'INSERT INTO todos (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
    'id': 2,
    'completed': False
}
cursor.execute(SQL, data)

# how to fetch data
cursor.execute('SELECT * from todos;')

result = cursor.fetchall()
print(result)

# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()
