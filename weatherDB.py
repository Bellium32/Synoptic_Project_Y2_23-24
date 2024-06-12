import mysql.connector
################Guide to establishing the connection##########################
#Have SQL Workbench, Installer, and Shell instealled on the device
#Have python and it's dependencies installed, if using VS studio install "MySQL Shell for VS Code"
#To establish the connection, press "Windows key + R", them type in "cmd"
#Type in: cd "C:\Users\emman\AppData\Local\Programs\Python\Python312\Scripts"
#If this doesn't work: cd "C:\Users\*yourusername*\AppData\Local\Programs\Python\" and find scripts from there
#Then copy in: pip install mysql-connector-python |or| python -m pip install mysql-connector-python

 
databaseExist = True
#If a database exists set this to true, if one doesn't, set to false and run to create the database
#After that run the create table function to create the tables of the database
global mydb
if databaseExist == False:
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE weatherdb")

else:
    #Connects the codebase to the database using this authentication
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="weatherdb"
    )
    
    #Creates a cursor object that allows us to pass commands to the database
    mycursor = mydb.cursor()

def my_Tables_Create():
    #SQL commands to create tables
    mycursor.execute("CREATE TABLE weatherDay (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(5), day VARCHAR(10), date VARCHAR(15),"
                     "meanTemp VARCHAR(7), minTemp VARCHAR(7), maxTemp VARCHAR(7), conditions VARCHAR(63))")
    mycursor.execute("CREATE TABLE weatherHour (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(5), hour VARCHAR(7), date VARCHAR(15),"
                    "meanTemp VARCHAR(7), minTemp VARCHAR(7), maxTemp VARCHAR(7), conditions VARCHAR(63))")
    mycursor.execute("CREATE TABLE people (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), phoneNumber VARCHAR(15))")

def my_Tables_Drop():
    #SQL commands to delete (drop) all tables
    mycursor.execute("DROP TABLE IF EXISTS weatherDay")
    mycursor.execute("DROP TABLE IF EXISTS weatherHour")
    mycursor.execute("DROP TABLE IF EXISTS people")
   
createAndDrop = 4
if createAndDrop == 1:
    print("Free space")
if createAndDrop == 2:
    my_Tables_Create()
if createAndDrop == 98:
    mycursor.execute("DROP DATABASE weatherdb")

if createAndDrop == 99:
    my_Tables_Drop()
    
def my_Day_Insert(location, day, date, meanTemp, minTemp, maxTemp, conditions):
    #Inserts data into the database, just pass the arguments into the commands 
    #So location = location etc
    sql = "INSERT INTO weatherDay (location, day, date, meanTemp, minTemp, maxTemp, conditions) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (location, day, date, meanTemp, minTemp, maxTemp, conditions)
    #values not only makes it easier to pass information from parameters
    #But also escapes the values to prevent sql injection
    mycursor.execute(sql, values)
    #Commits the changes into the database
    mydb.commit()
    #Tells user if records where inserted
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
    #Finds the data from within the database that matches the parameters
    sql = "SELECT * FROM weatherDay WHERE location = %s AND date = %s"
    values = (dataL, dataD, ) 
    mycursor.execute(sql, values)
    #Fetches all results that matches the query
    myresult = mycursor.fetchall()
    if myresult == []:
        print("nuh uh")
        return False
    #Prints all results that matches the query
    for p in myresult:
        print(p)
    return True

def my_Hour_Select(dataL, dataD, dataH):
    sql = "SELECT * FROM weatherHour WHERE location = %s AND date = %s AND hour = %s"
    values = (dataL, dataD, dataH) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    if myresult == []:
        print("nuh uh")
    for p in myresult:
        print(p)

def my_People_Select(data):
    sql = "SELECT * FROM people WHERE phoneNumber = %s"
    values = (data, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    if myresult == []:
        print("nuh uh")
        return False
    for p in myresult:
        print(p)

def my_Day_Update_Con(dataC, dataL, dataD, ):
    #Updates the database for the weather conditions on that day + location
    sql = "UPDATE weatherDay SET conditions = %s WHERE location = %s AND date = %s"
    values = (dataC, dataL, dataD, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")    
    
def my_Day_Update_Temp(dataTMe, dataTMi, dataTMa, dataL, dataD, ):
    #Updates the database for the temperature on that day + location
    sql = "UPDATE weatherDay SET meanTemp = %s, minTemp = %s, maxTemp = %s WHERE location = %s AND date = %s"
    values = (dataTMe, dataTMi, dataTMa, dataL, dataD, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")    
    
def my_Hour_Update_Con(dataC, dataL, dataD, dataH, ):
    sql = "UPDATE weatherHour SET conditions = %s WHERE location = %s AND date = %s AND hour = %s"
    values = (dataC, dataL, dataD, dataH, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")  
    
def my_Hour_Update_Temp(dataTMe, dataTMi, dataTMa, dataL, dataD, dataH, ):
    sql = "UPDATE weatherHour SET meanTemp = %s, minTemp = %s, maxTemp = %s WHERE location = %s AND date = %s AND hour = %s"
    values = (dataTMe, dataTMi, dataTMa, dataL, dataD, dataH, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")  
        
if createAndDrop == 3:                   
    my_Day_Insert("PN", "Monday", "2024-06-06", "26.3", "24.1", "29.9", "light rain")
    my_Hour_Insert("MO", "09:00", "2024-06-06", "27.8", "25.2", "30.1", "sunny outside")
    my_people_Insert("Timmothy", "Smith", "071411 26345")

if createAndDrop == 4:
    my_Day_Select("PN", '2024-06-06')

if createAndDrop == 5:
    my_Day_Insert("PN", "Tuesday", "2024-06-07", "27.3", "23.6", "34.3", "light rain")

if createAndDrop == 6:
    my_Hour_Select("MO", '2024-06-06', "09:00")

if createAndDrop == 7:
    my_People_Select("071411 26345")
    
if createAndDrop == 8:
    my_Day_Update_Con("heavy rain","PN", "2024-06-06")
    my_Day_Update_Temp("27.3", "21.6", "34.3","PN", "2024-06-06")
    my_Hour_Update_Con("heavy rain","MO", "2024-06-06", "09:00")

if createAndDrop == 9:
    my_Day_Select("MO", "Teheehee")


#mycursor.execute("SHOW TABLES")



