Here the sqlite3 is used which is available without installing anything.
There are two ways it can be used.
1- creating a database file in the current dir and creating a table in that file
2- using in-Memory database
TO read about the notes on sqlite
https://www.sqlite.org/datatype3.html
import sqlite3
conn = sqlite3.connect('employee.db')   
c=conn.cursor()
c.execute("""CREATE TABLE employee (
                     first    text,
                     last     text,
                     pay      integer)
          """)
conn.commit()
conn.close()
2-
conn = sqlite3.connect(':memory:')


import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST book (id INTEGER PRIMARY KEY, title text,
                 author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book  WHERE title=? OR author=? 
                 OR year=? or ISBN=?",(title,author,year, isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE from book  WHERE id =?",(id))
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE from book SET title= ?,author =?, year =?, isbn =?
                 WHERE id =?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()