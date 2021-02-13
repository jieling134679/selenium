标准数据库接口：DB-API(cx_oracle)

引入API接口
获取与数据库的连接
执行SQL语句和存储过程
关闭数据库连接

import cx_Oracle
#用户/密码/IP/实例名称
#conn连接对象
conn = cx_Oracle.connect('afa/afa2018@15.0.20.19/ensemble')

连接对象conn的常用方法：
1.commit()     提交
2.rollback()   回滚
3.cursor()     创建游标
4.close()      关闭连接

游标cursor的常用属性和方法：
1.fetchone()     获取到一条记录
2.fetchmany(n)   获取n条记录
3.fetchall()     获取全部记录
4.close()        关闭游标


#创建连接
cursor = conn.cursor()
cursor.execute("select * from afa.t_beps_paymentbook")
row = cursor.fetchone()
#打印取出的一行的第一列的数据
print(row[0])
cursor.close()
conn.close()

#insert举例
cursor.execute(insert into afa.t_beps_paymentbook values ('aaa', 'bbb', 'ccc'))
conn.commit()

#循环多条
cursor.execute("select * from afa.t_beps_paymentbook")
rows = cursor.fetchmany(20)
for row in rows:
    print("%d %s %s %s " %(row[0], row[1], row[2], row[3]))
print("number of the rows is $d" , % cursor.rowcount)

#循环多条
cursor.execute("SELECT *FROM TEST")
while(1):
    row = cursor.fetchone()
	if row == null:
	    break
	

