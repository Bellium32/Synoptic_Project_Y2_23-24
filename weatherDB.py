import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="weatherdb"
)
mycursor = mydb.cursor()

createAndDrop = 4
if createAndDrop == 1:
    mycursor.execute("CREATE DATABASE weatherdb")
if createAndDrop == 2:
    mycursor.execute("CREATE TABLE weatherDay (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(255), day VARCHAR(10), date VARCHAR(15),"
                     "meanTemp VARCHAR(4), minTemp VARCHAR(4), maxTemp VARCHAR(4), conditions VARCHAR(63))")
    mycursor.execute("CREATE TABLE weatherHour (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(255), hour VARCHAR(7), date VARCHAR(15),"
                    "meanTemp VARCHAR(4), minTemp VARCHAR(4), maxTemp VARCHAR(4), conditions VARCHAR(63))")
    mycursor.execute("CREATE TABLE people (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), phoneNumber VARCHAR(15))")

if createAndDrop == 99:
    mycursor.execute("DROP TABLE IF EXISTS weatherDay")
    mycursor.execute("DROP TABLE IF EXISTS weatherHour")
    mycursor.execute("DROP TABLE IF EXISTS people")
   
def my_Day_Insert(location, day, date, meanTemp, minTemp, maxTemp, conditions):
    sql = "INSERT INTO weatherDay (location, day, date, meanTemp, minTemp, maxTemp, conditions) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (location, day, date, meanTemp, minTemp, maxTemp, conditions)
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def my_Hour_Insert(location, hour, date, meanTemp, minTemp, maxTemp, conditions):
    sql = "INSERT INTO weatherHour (location, hour, date, meanTemp, minTemp, maxTemp, conditions) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (location, hour, date, meanTemp, minTemp, maxTemp, conditions)
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
def my_people_Insert(fname, lname, phoneNumber):
    sql = "INSERT INTO people (fname, lname, phoneNumber) VALUES (%s, %s, %s)"
    values = (fname, lname, phoneNumber)
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def my_Day_Select(dataL, dataD):
    sql = "SELECT * FROM weatherDay WHERE location = %s AND date = %s"
    values = (dataL, dataD, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)

def my_Hour_Select(dataL, dataD, dataH):
    sql = "SELECT * FROM weatherHour WHERE location = %s AND date = %s AND hour = %s"
    values = (dataL, dataD, dataH) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)

def my_People_Select(data):
    sql = "SELECT * FROM people WHERE phoneNumber = %s"
    values = (data, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)

if createAndDrop == 3:                   
    my_Day_Insert("PN", "Monday", "2024-06-06", "26.3", "24.1", "29.9", "light rain")
    my_Hour_Insert("MO", "09:00", "2024-06-06", "27.8", "25.2", "30.1", "sunny outside")
    my_people_Insert("Timmothy", "Smith", "071411 26345")

if createAndDrop == 4:
    my_Day_Select("PN", '2024-06-07')

if createAndDrop == 5:
    my_Day_Insert("PN", "Tuesday", "2024-06-07", "27.3", "23.6", "34.3", "light rain")

if createAndDrop == 6:
    my_Hour_Select("MO", '2024-06-06', "09:00")

if createAndDrop == 7:
    my_People_Select("071411 26345")


mycursor.execute("SHOW TABLES")



