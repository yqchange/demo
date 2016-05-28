import psycopg2


conn = psycopg2.connect(host='localhost', 
	database="hw04", user="dbo", password="123456")

cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a  (
    sn       INTEGER,    --序号
    name     TEXT,       --姓名
    PRIMARY KEY(sn)
    )
	''')


cur.execute('''
		INSERT INTO hw_a (sn, name) VALUES
		(10, 'A10'),
		(20, 'A20'),
	        (30, 'A30'),
		(40, 'A40'),
		(50, 'A50'),
		(60, 'A60')
	''')

cur.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b  (
    sn       INTEGER,    --序号
    name     TEXT,       --姓名
    PRIMARY KEY(sn)
    )
	''')


cur.execute('''
		INSERT INTO hw_b (sn, name) VALUES
		(40, 'B40'),
		(50, 'B50'),
	        (60, 'B60'),
		(70, 'B70'),
		(80, 'B80')
	''')
conn.commit()

