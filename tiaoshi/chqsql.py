import pymysql
conn= pymysql.connect(
host='139.196.133.170',
port = 3306,
user='jftestuser',
passwd='quton8RFKLuZynOV48yzyePnKZKBGz',
db ='jftest-t',
)

cur = conn.cursor()     # 获取一个游标
sql = "SELECT borrow_id FROM rd_borrow_tender where user_id = 1687 Order BY add_time DESC LIMIT 1"
cur.execute(sql)
"""
for a in cur.fetchall():
    print(a)

#cur.close()
conn.close()
"""



r = cur.fetchall()  #将所有查询结果返回为元组

for a in r:
    #print(r)

    user_host =a[0]

   #sql_text =a[1]

    print ("%s" %(user_host))
    #print(user_host+1)
conn.close()



