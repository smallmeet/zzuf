#encoding:utf-8
import sqlite3

db = sqlite3.connect('database_test.db')
c = db.cursor()
try:
    c.execute('create table tesst(key,var)')
except:
    print "Table exist or DB Error"
    
c.execute('insert into test values(?, ?)',('sss','ssss'))
db.commit()
c.execute('select * from test')
print c.fetchall()
c.execute('select name from sqlite_master')
z = c.fetchall()
for ret in z:
    if 'test' in ret:
        print 'Success'
c.close()
db.close()