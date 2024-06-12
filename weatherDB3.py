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
    mycursor.execute("CREATE DATABASE weatherdb3")

else:
    #Connects the codebase to the database using this authentication
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="weatherdb3"
    )
    
    #Creates a cursor object that allows us to pass commands to the database
    mycursor = mydb.cursor()
    databaseRECORD = False
def my_Tables_Create():
    #SQL commands to create tables
    mycursor.execute("CREATE TABLE weatherDay (wDayId INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(5), day VARCHAR(10), date DATE,"
                     "weatherData TEXT)")
    mycursor.execute("CREATE TABLE weatherHour (wHourId INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(5), hour TIME, date DATE,"
                     "weatherData TEXT)")
    mycursor.execute("CREATE TABLE people (peopleId INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), phoneNumber VARCHAR(15))")
    
    mycursor.execute("CREATE TABLE weatherTemp (wTempId INT AUTO_INCREMENT PRIMARY KEY,temp DECIMAL(2,2), feels_like DECIMAL(2,2), temp_min DECIMAL(2,2), "
                     "temp_max DECIMAL(2,2), pressure INT, sea_level INT, grnd_level INT, humidity INT, temp_kf DECIMAL(2,2))")                  
    mycursor.execute("CREATE TABLE weatherStats (wStatsId INT AUTO_INCREMENT PRIMARY KEY, weather_id INT, weather_main VARCHAR(25), "
                     "weather_description VARCHAR(50), weather_icon VARCHAR(10))")
    mycursor.execute("CREATE TABLE weatherWind (wWindId INT AUTO_INCREMENT PRIMARY KEY, wind_speed DECIMAL(2,2), wind_deg INT, wind_gust DECIMAL(2,2))")
    
    mycursor.execute("CREATE TABLE weatherInfo (wDataId INT AUTO_INCREMENT PRIMARY KEY, dt INT, wTempId INT, wStatsId INT, wWindId INT, "
                     " FOREIGN KEY (wTempId) REFERENCES weatherTemp(wTempId), FOREIGN KEY (wStatsId) REFERENCES weatherStats(wStatsId), "
                     "clouds_all INT, FOREIGN KEY (wWindId) REFERENCES weatherWind(wWindId), visibility INT, pop FLOAT, "
                     "rain_3h DECIMAL(2,2), sys_pod VARCHAR(5), dt_txt DATETIME)")
    
    
  


def my_Tables_Drop():
    #SQL commands to delete (drop) all tables
    mycursor.execute("DROP TABLE IF EXISTS weatherDay")
    mycursor.execute("DROP TABLE IF EXISTS weatherHour")
    mycursor.execute("DROP TABLE IF EXISTS people")
    mycursor.execute("DROP TABLE IF EXISTS weatherInfo")
    mycursor.execute("DROP TABLE IF EXISTS weatherTemp")
    mycursor.execute("DROP TABLE IF EXISTS weatherStats")
    mycursor.execute("DROP TABLE IF EXISTS weatherWind")
    
def my_Tables_Truncate():
    mycursor.execute("TRUNCATE TABLE weatherDay")
    mycursor.execute("TRUNCATE TABLE weatherHour")
    mycursor.execute("TRUNCATE TABLE weatherInfo")
    mycursor.execute("TRUNCATE TABLE weatherTemp")
    mycursor.execute("TRUNCATE TABLE weatherStats")
    mycursor.execute("TRUNCATE TABLE weatherWind")
   
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
        
def my_WeatherInfo_Insert(dt, wTempId, wStatsId, clouds_all, wWindId, visibility, pop, rain_3h, sys_pod, dt_txt):
    sql = """
    INSERT INTO weatherInfo (
        dt, wTempId, wStatsId, clouds_all, wWindId, visibility, pop, rain_3h, sys_pod, dt_txt
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (dt, wTempId, wStatsId, clouds_all, wWindId, visibility, pop, rain_3h, sys_pod, dt_txt)
    mycursor.execute(sql, values)
    mydb.commit()
    if databaseRECORD:
        print(mycursor.rowcount, "record inserted.")
        
        
def my_WeatherTemp_Insert(temp, feels_like, temp_min, temp_max, pressure, sea_level, grnd_level, humidity, temp_kf):
    sql = "INSERT INTO weatherTemp (temp, feels_like, temp_min, temp_max, pressure, sea_level, grnd_level, humidity, temp_kf) VALUES (%d, %d, %d, %d, %d, %d, %d, %d, %d)"
    values = (temp, feels_like, temp_min, temp_max, pressure, sea_level, grnd_level, humidity, temp_kf)
    mycursor.execute(sql, values)
    mydb.commit()
    if databaseRECORD:
        print(mycursor.rowcount, "record inserted.")
               
def my_WeatherStats_Insert(weather_id, weather_main, weather_description, weather_icon):
    sql = "INSERT INTO weatherStats (weather_id, weather_main, weather_description, weather_icon) VALUES (%d, %s, %s, %s)"
    values = (weather_id, weather_main, weather_description, weather_icon)
    mycursor.execute(sql, values)
    mydb.commit()
    if databaseRECORD:
        print(mycursor.rowcount, "record inserted.")
      
def my_WindData_Insert(wind_speed, wind_deg, wind_gust):
    sql = "INSERT INTO weatherWind (wind_speed, wind_deg, wind_gust) VALUES (%d, %d, %d)"
    values = (wind_speed, wind_deg, wind_gust)
    mycursor.execute(sql, values)
    mydb.commit()
    if databaseRECORD:
        print(mycursor.rowcount, "record inserted.")
        
if createAndDrop == 3:                   
    my_Day_Insert("PN", "Monday", "2024-06-06", "2114")
    my_Hour_Insert("MO", "09:00", "2024-06-06", "6885")
    my_people_Insert("Timmothy", "Smith", "071411 26345")

if createAndDrop == 4:
    my_Day_Select_WeatherID("PN", '2024-06-13')

if createAndDrop == 5:
    my_Day_Insert("PN", "Tuesday", "2024-06-07", "8442")

if createAndDrop == 6:
    print("Jooe")
    #my_Hour_Select("MO", '2024-06-08', "09:00")

if createAndDrop == 7:
    my_People_Select("071411 26345")
    
if createAndDrop == 8:
    my_Day_Update_Weather("4855","PN", "2024-06-06")
    my_Hour_Update_Weather("2008","MO", "2024-06-06", "09:00")

if createAndDrop == 9:
    my_Day_Select_Check("MO", "Teheehee")


#mycursor.execute("SHOW TABLES")



