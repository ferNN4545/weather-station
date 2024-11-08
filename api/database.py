'''
Nombre F
Scrpt description: weather-station Database 
engine: SQLite 3
Date: 9/9/24
'''
#import database engine  package
import sqlite3


#create weather-station database connection
con = sqlite3.connect('weather-station.db')

#created cursor
cur = con.cursor()

#users model
users_model ='''
    CREATE TABLE IF NOT EXISTS users (
  id integer PRIMARY KEY,
  username TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 1,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  status BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
  update_at TIMESTAMP DEFAULT (datetime('now','localtime')),
  deleted_at NULL
  )




'''


# Execute query
cur.execute(users_model)


#close connection
#con.close()
    
