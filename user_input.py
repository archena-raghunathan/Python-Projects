#!c:/Python27/python.exe

print ("Content-type: text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Enter your input</title>')
print ('</head>')
print ('<body bgcolor = "#FFBF00">')
print ('<h2><font face="Monotype corsiva" size = 6 color = "#8A0829"><I>"View your initial TICTACTOE table with positions from 1 to 9."</I></font></h2>')
print ('<h2><font face="Monotype corsiva" size = 6 color = "Green"><I>"To start a new game click on TICTACTOE"</I></font>')
print ('<form name="pyform" method="post" action="/cgi-bin/original_tictactoe_table.py"><br>')
print ('<input type="submit" style="height:50px; width:200px; name="submit" value = TICTACTOE>')
print ('</form>')
print ('<h2><font face="Times new Roman" size = 5.5 color = "blue"><I>"Select Player Option: O or X ?</I></font></h2>')
print ('<form name="pyform" method="post" action="/cgi-bin/mysql_tic_tac_toe.py"><br>')
print ('<input type="text" name="player_name"><br>')
print ('<br>')
print ('<h2><font face="Times New Roman" size = 5.5 color = "blue"><I>Select your position on the grid from (1 to 9): </I></font></h2>')
#print ('<form name="pyform" method="post" action="/cgi-bin/mysql_tic_tac_toe.py"><br>')
print ('<input type="text" name="move"><br>')
print ('<br>')
print ('<br>')
print ('<br>')
print ('<input type="submit" style="height:50px; width:175px; name="submit" value = Submit>')
print ('</form>')
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
print ('</body>')
print ('</html>')
