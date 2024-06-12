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
global databaseRECORD
if databaseExist == False:
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE weatherdb2")

else:
    #Connects the codebase to the database using this authentication
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="weatherdb2"
    )
    
    #Creates a cursor object that allows us to pass commands to the database
    mycursor = mydb.cursor()
    databaseRECORD = False
def my_Tables_Create():
    #SQL commands to create tables
    mycursor.execute("CREATE TABLE weatherDay (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(5), day VARCHAR(10), date DATE,"
                     "weatherData TEXT)")
    mycursor.execute("CREATE TABLE weatherHour (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(5), hour TIME, date DATE,"
                     "weatherData TEXT)")
    mycursor.execute("CREATE TABLE people (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), phoneNumber VARCHAR(15))")

def my_Tables_Drop():
    #SQL commands to delete (drop) all tables
    mycursor.execute("DROP TABLE IF EXISTS weatherDay")
    mycursor.execute("DROP TABLE IF EXISTS weatherHour")
    mycursor.execute("DROP TABLE IF EXISTS people")
    
def my_Tables_Truncate():
    mycursor.execute("TRUNCATE TABLE weatherDay")
    mycursor.execute("TRUNCATE TABLE weatherHour")
   
createAndDrop = 0
if createAndDrop == 1:
    print("Free space")
if createAndDrop == 2:
    my_Tables_Create()
    
if createAndDrop == 97:
    my_Tables_Truncate()
    
if createAndDrop == 98:
    mycursor.execute("DROP DATABASE weatherdb2")

if createAndDrop == 99:
    my_Tables_Drop()
    
def my_Day_Insert(location, day, date, weatherData):
    #Inserts data into the database, just pass the arguments into the commands 
    #So location = location etc
    sql = "INSERT INTO weatherDay (location, day, date, weatherData) VALUES (%s, %s, %s, %s)"
    values = (location, day, date, weatherData)
    #values not only makes it easier to pass information from parameters
    #But also escapes the values to prevent sql injection
    mycursor.execute(sql, values)
    #Commits the changes into the database
    mydb.commit()
    #Tells user if records where inserted
    if databaseRECORD == True:
        print(mycursor.rowcount, "record inserted.")

def my_Hour_Insert(location, hour, date, weatherData):
    sql = "INSERT INTO weatherHour (location, hour, date, weatherData) VALUES (%s, %s, %s, %s)"
    values = (location, hour, date, weatherData)
    mycursor.execute(sql, values)
    mydb.commit()
    if databaseRECORD == True:
        print(mycursor.rowcount, "record inserted.")
    
def my_people_Insert(fname, lname, phoneNumber):
    sql = "INSERT INTO people (fname, lname, phoneNumber) VALUES (%s, %s, %s)"
    values = (fname, lname, phoneNumber)
    mycursor.execute(sql, values)
    mydb.commit()
    if databaseRECORD == True:
        print(mycursor.rowcount, "record inserted.")

def my_Day_Select_Check(dataL, dataD):
    #Finds the data from within the database that matches the parameters
    sql = "SELECT * FROM weatherDay WHERE location = %s AND date = %s"
    values = (dataL, dataD, ) 
    mycursor.execute(sql, values)
    #Fetches all results that matches the query
    myresult = mycursor.fetchall()
    if myresult == []:      
        return False
    return True

def my_Day_Select_WeatherID(dataL, dataD):
    #Finds the data from within the database that matches the parameters
    sql = "SELECT weatherData FROM weatherDay WHERE location = %s AND date = %s"
    values = (dataL, dataD, ) 
    mycursor.execute(sql, values)
    #Fetches all results that matches the query
    myresult = mycursor.fetchone()
    # if myresult == []:
    #     print("nuh uh")
    #     return False
    #Prints all results that matches the query
    # for p in myresult:
    #     print(p)
    return myresult

def my_Hour_Select_Check(dataL, dataD, dataH):
    sql = "SELECT * FROM weatherHour WHERE location = %s AND date = %s AND hour = %s"
    values = (dataL, dataD, dataH) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    if myresult == []:
        return False
        #print("nuh uh")
    return True

def my_Hour_Select_WeatherID(dataL, dataD, dataH):
    #Finds the data from within the database that matches the parameters
    sql = "SELECT weatherData FROM weatherHour WHERE location = %s AND date = %s AND hour = %s"
    values = (dataL, dataD, dataH) 
    mycursor.execute(sql, values)
    #Fetches all results that matches the query
    myresult = mycursor.fetchone()
    # if myresult == []:
    #     print("nuh uh")
    #     return False
    #Prints all results that matches the query
    # for p in myresult:
    #     print(p)
    return myresult

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

def my_Day_Update_Weather(dataW, dataL, dataD, ):
    #Updates the database for the weatherData on that day + location
    sql = "UPDATE weatherDay SET weatherData = %s WHERE location = %s AND date = %s"
    values = (dataW, dataL, dataD, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)
    mydb.commit()
    if databaseRECORD == True:
        print(mycursor.rowcount, "record(s) affected")    
     
    
def my_Hour_Update_Weather(dataW, dataL, dataD, dataH, ):
    sql = "UPDATE weatherHour SET weatherData = %s WHERE location = %s AND date = %s AND hour = %s"
    values = (dataW, dataL, dataD, dataH, ) 
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    for p in myresult:
        print(p)
    mydb.commit()
    if databaseRECORD == True:
        print(mycursor.rowcount, "record(s) affected")  
        
if createAndDrop == 3:                   
    my_Day_Insert("PN", "Monday", "2024-06-06", "2114")
    my_Hour_Insert("MO", "09:00", "2024-06-06", "6885")
    my_people_Insert("Timmothy", "Smith", "071411 26345")

if createAndDrop == 4:
    my_Day_Select_WeatherID("PN", '2024-06-13')

if createAndDrop == 5:
    my_Day_Insert("PN", "Tuesday", "2024-06-07", "8442")

if createAndDrop == 6:
    my_Hour_Select("MO", '2024-06-08', "09:00")

if createAndDrop == 7:
    my_People_Select("071411 26345")
    
if createAndDrop == 8:
    my_Day_Update_Weather("4855","PN", "2024-06-06")
    my_Hour_Update_Weather("2008","MO", "2024-06-06", "09:00")

if createAndDrop == 9:
    my_Day_Select_Check("MO", "Teheehee")


#mycursor.execute("SHOW TABLES")



