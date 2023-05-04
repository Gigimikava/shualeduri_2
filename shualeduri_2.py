#n1
# import sqlite3
# conn = sqlite3.connect("survey.sqlite")
# cursor=conn.cursor()

# select_result = cursor.execute("SELECT * FROM students")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)

# select_result = cursor.execute("SELECT count(id) as count_students from students where SelfStudyHour < 2")
# print(select_result)

# def x(device, age):
#     st=cursor.execute("SELECT count(id) from students where device = :device_con  AND age = :age_con",{"device_con":device,"age_con":age})
#     for row in st:
#         list(row)
#         print(row[0])

# select_result=cursor.execute("INSERT into students(age,OnlineClassTime,Device,SelfStudyHour,FitnessTime,Sleep,SocialMedia,SocialMediaPlatform) VALUES (15,2,'Laptop',3,4,6,4,'TikTok')")
# conn.commit()
#
# select_result=cursor.execute("UPDATE students SET device='Nokia Teleponi' WHERE age <> 21 ")
# conn.commit()


#n2
# import json
# with open('sample.json') as sample:
#     data = json.load(sample)


