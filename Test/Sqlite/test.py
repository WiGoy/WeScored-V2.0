import sqlite3

#  建库
cx = sqlite3.connect('D:\\WorkspaceGit\\WeScored-V2.0\\Test\\Sqlite\\test.db')

#  建表
cu=cx.cursor()
'''
cu.execute("""create table catalog ( id integer primary key, pid integer, name varchar(10) UNIQUE )""")

#  插入
cu.execute("insert into catalog values(0, 0, 'name1')")   
cu.execute("insert into catalog values(1, 0, 'hello')")   
cx.commit()

#  选择
cu.execute("select * from catalog")   
print(cu.fetchall())
cu.execute("select * from catalog where id = 1")   
print(cu.fetchone()) 
'''
#   修改
cu.execute("update catalog set name='name2' where id = 0")   
cx.commit()   
cu.execute("select * from catalog")   
print(cu.fetchone())

#  删除
cu.execute("delete from catalog where id = 1")
cx.commit()
cu.execute("select * from catalog")
cu.fetchall()
#cu.close()  
#cx.close()