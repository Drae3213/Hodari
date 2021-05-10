'''
**************************************************************
  Program  lessson_5.py
  Author   Baba
  Date     March 13, 2021

  Description:
  This program is used to introduce Geniuses to using a 
  database Structured Query Language (SQL).  The program
  imports the sqlite3 module which allows you to create
  and interact with an SQL Database

  - The create_connection function is passed the
    path of the SQLite database file then it connects 
    the app to an exixting SQLite3 database named hgp_pods 
    or if it;s not present it creates the database file
  
  - The execute_query function is passed the path and the 
    query to implement; create_staff_member_table query and
    add_staff_member query

  - The execute_read function is passed the path and 
    the display_staff_member query
**************************************************************

'''

import sqlite3
from sqlite3 import Error

############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


###################  Connect to The Database File *********************
connection = create_connection("/users/andrewlubega/sql_tutorial/oak8_pods.sqlite")


##########################  Create And Execute Queries ################
create_staff_member_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_staff_member_table_query) 

add_staff = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980)','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeem','(415) 684-0505','Programs Director');
"""
execute_query(connection, add_staff)

#Leaders

create_leader_member_table_query = """
CREATE TABLE IF NOT EXISTS leader (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_leader_member_table_query) 

add_leader = """
INSERT INTO
  leader (name,cell,position)
VALUES
  ('Andrew','925.727.4611)','editor'),
  ('Jacore','111.111.1111', 'producer'),
  ('Aris','(510) 435-2594','aries'),
  ('Richard','(415) 684-0505','richie'),
  ('Gabe','925.727.4611)','gabiru'),
  ('JAHI', '9293203920','JAHYEET');
"""
execute_query(connection, add_leader)

#Members

create_members_member_table_query = """
CREATE TABLE IF NOT EXISTS members (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_members_member_table_query) 

add_members = """
INSERT INTO
  members (name,cell,position)
VALUES
  ('Drae','925.727.4611)','lead'),
  ('Glenn','111.111.1111', 'dat boy'),
  ('Malick','(510) 435-2594','light'),
  ('Ronin','(415) 684-0505','ninja');
"""
execute_query(connection, add_members)

########################### Display staff_member Query ##################### 
display_staff_query = "SELECT * from staff "
staff = execute_read_query(connection, display_staff_query)

for user in staff:
    print(user)
print("\n")
execute_query(connection, "drop table staff")


display_leader_query = "SELECT * from leader"
leader = execute_read_query(connection, display_leader_query)

for user in leader:
    print(user)
print("\n")

execute_query(connection, "drop table leader")
	
display_members_query = "SELECT * from members"
members = execute_read_query(connection, display_members_query)

for user in members:
    print(user)
print("\n")

execute_query(connection, "drop table members")
