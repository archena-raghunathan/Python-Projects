#!c:/Python27/python.exe

print ("Content-type: text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<body bgcolor = "E5F71C">')
print ('<h1><font face="Arial" size = 6 color = "Purple"><I>Tic Tac Toe!!</I> </font></h1>')
print ('<h3><font face="Times new Roman" size = 5 color = "green">"Description of this tic tac toe game!!"</font></h3>')
print ('<font face="Monotype Corsiva" size = 6 color = "blue">"Tic-tac-toe is a grid game for two players, X and O, who take turns marking the spaces in a 3X3 grid."</font>')
print ('<font face="Monotype Corsiva" size = 6 color = "blue">"The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game."</font>')
print ('<br>')
print ('<br>')
print ('<br>')

import cgi,cgitb
import random
cgitb.enable() #for debugging
form = cgi.FieldStorage()
import HTML
import MySQLdb
db= MySQLdb.connect(user='archena',passwd='1234',host='localhost',db='myschema')
cur = db.cursor()
def original_table():
    cur.execute("UPDATE tictactoe SET col1 = 1 WHERE id = 1")
    cur.execute("UPDATE tictactoe SET col2 = 2 WHERE id = 1")
    cur.execute("UPDATE tictactoe SET col3 = 3 WHERE id = 1")
    cur.execute("UPDATE tictactoe SET col1 = 4 WHERE id = 2")
    cur.execute("UPDATE tictactoe SET col2 = 5 WHERE id = 2")
    cur.execute("UPDATE tictactoe SET col3 = 6 WHERE id = 2")
    cur.execute("UPDATE tictactoe SET col1 = 7 WHERE id = 3")
    cur.execute("UPDATE tictactoe SET col2 = 8 WHERE id = 3")
    cur.execute("UPDATE tictactoe SET col3 = 9 WHERE id = 3")
    cur.execute("COMMIT")
    cur.execute("SELECT col1,col2,col3 FROM tictactoe")
    # print (cur.fetchall())
    table_data = cur.fetchall()
    # print list(table_data)
    htmlcode = HTML.table(table_data)
    return htmlcode


htmlcode = original_table()
print ('<h2><b>')
print (htmlcode)
print ('</b></h2>')
print ('<form name="pyform" method="post" action="/cgi-bin/user_input.py"><br>')
print ('<input type="submit" style="height:50px; width:150px; name="submit" value = "User Input Page">')
print ('</form>')
print ('</body>')
print ('</head>')
print ('</html>')