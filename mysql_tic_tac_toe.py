#!c:/Python27/python.exe

print ("Content-type: text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<body bgcolor = "#81F7F3">')
import cgi,cgitb
import random
cgitb.enable() #for debugging
form = cgi.FieldStorage()
import HTML
import MySQLdb
db= MySQLdb.connect(user='archena',passwd='1234',host='localhost',db='myschema')
cur = db.cursor()
#cur.execute("CREATE TABLE tictactoe (col1 int, col2 int , col3 int)")
#cur.execute("INSERT INTO tictactoe VALUES(4,5,6)")
#cur.execute("SHOW TABLES")
#chances = 9
#while chances > 0:
def owin(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] == 'O' or grid[1][0] == grid[1][1] == grid[1][2] == 'O' or grid[2][0] == grid[2][1] == grid[2][2] == 'O' or grid[0][0] == grid[1][0] == grid[2][0] == 'O' or grid[0][1] == grid[1][1] == grid[2][1] == 'O' or grid[0][2] == grid[1][2] == grid[2][2] == 'O' or grid[0][0] == grid[1][1] == grid[2][2] == 'O' or grid[0][2] == grid[1][1] == grid[2][0] == 'O':
        return True
    else:
        return False
def xwin(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] == 'X' or grid[1][0] == grid[1][1] == grid[1][2] == 'X' or grid[2][0] == grid[2][1] == grid[2][2] == 'X' or grid[0][0] == grid[1][0] == grid[2][0] == 'X' or grid[0][1] == grid[1][1] == grid[2][1] == 'X' or grid[0][2] == grid[1][2] == grid[2][2] == 'X' or grid[0][0] == grid[1][1] == grid[2][2] == 'X' or grid[0][2] == grid[1][1] == grid[2][0] == 'X':
        return True
    else:
        return False
def tie(grid):
    if grid[0][0] in ('O', 'X') and grid[0][1] in ('O', 'X') and grid[0][2] in ('O', 'X') and grid[1][0] in ('O', 'X') and grid[1][1] in ('O', 'X') and grid[1][2] in ('O', 'X') and grid[2][0] in ('O', 'X') and grid[2][1] in ('O', 'X') and grid[2][2] in ('O', 'X'):
        return True
    else:
        return False

def table_entries(move,player):
    #col_pos = ""
    if player == "O":
        if pos == '1':
            cur.execute("SELECT col1 FROM tictactoe WHERE id = 1")
            col_pos = cur.fetchall()
            #print "Data" , col_pos[0][0]
            if col_pos[0][0] == '1':
                cur.execute("UPDATE tictactoe SET col1 = 'O' WHERE id = 1 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '2':
            cur.execute("SELECT col2 FROM tictactoe WHERE id = 1")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '2':
                cur.execute("UPDATE tictactoe SET col2 = 'O' WHERE id = 1 ")
                cur.execute("COMMIT")
            else:
                print(
                '<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '3':
            cur.execute("SELECT col3 FROM tictactoe WHERE id = 1")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '3':
                cur.execute("UPDATE tictactoe SET col3 = 'O' WHERE id = 1 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '4':
            cur.execute("SELECT col1 FROM tictactoe WHERE id = 2")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '4':
                cur.execute("UPDATE tictactoe SET col1 = 'O' WHERE id = 2 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '5':
            cur.execute("SELECT col2 FROM tictactoe WHERE id = 2")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '5':
                cur.execute("UPDATE tictactoe SET col2 = 'O' WHERE id = 2 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '6':
            cur.execute("SELECT col3 FROM tictactoe WHERE id = 2")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '6':
                cur.execute("UPDATE tictactoe SET col3 = 'O' WHERE id = 2 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '7':
            cur.execute("SELECT col1 FROM tictactoe WHERE id = 3")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '7':
                cur.execute("UPDATE tictactoe SET col1 = 'O' WHERE id = 3 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '8':
            cur.execute("SELECT col2 FROM tictactoe WHERE id = 3")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '8':
                cur.execute("UPDATE tictactoe SET col2 = 'O' WHERE id = 3 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        elif pos == '9':
            cur.execute("SELECT col3 FROM tictactoe WHERE id = 3")
            col_pos = cur.fetchall()
            #print "Data", col_pos[0][0]
            if col_pos[0][0] == '9':
                cur.execute("UPDATE tictactoe SET col3 = 'O' WHERE id = 3 ")
                cur.execute("COMMIT")
            else:
                print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
        else:
            print "None"
    else:
        if player == "X":
            if pos == '1':
                cur.execute("SELECT col1 FROM tictactoe WHERE id = 1")
                col_pos = cur.fetchall()
                # print "Data" , col_pos[0][0]
                if col_pos[0][0] == '1':
                    cur.execute("UPDATE tictactoe SET col1 = 'X' WHERE id = 1 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '2':
                cur.execute("SELECT col2 FROM tictactoe WHERE id = 1")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '2':
                    cur.execute("UPDATE tictactoe SET col2 = 'X' WHERE id = 1 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '3':
                cur.execute("SELECT col3 FROM tictactoe WHERE id = 1")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '3':
                    cur.execute("UPDATE tictactoe SET col3 = 'X' WHERE id = 1 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '4':
                cur.execute("SELECT col1 FROM tictactoe WHERE id = 2")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '4':
                    cur.execute("UPDATE tictactoe SET col1 = 'X' WHERE id = 2 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '5':
                cur.execute("SELECT col2 FROM tictactoe WHERE id = 2")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '5':
                    cur.execute("UPDATE tictactoe SET col2 = 'X' WHERE id = 2 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '6':
                cur.execute("SELECT col3 FROM tictactoe WHERE id = 2")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '6':
                    cur.execute("UPDATE tictactoe SET col3 = 'X' WHERE id = 2 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '7':
                cur.execute("SELECT col1 FROM tictactoe WHERE id = 3")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '7':
                    cur.execute("UPDATE tictactoe SET col1 = 'X' WHERE id = 3 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '8':
                cur.execute("SELECT col2 FROM tictactoe WHERE id = 3")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '8':
                    cur.execute("UPDATE tictactoe SET col2 = 'X' WHERE id = 3 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')
            elif pos == '9':
                cur.execute("SELECT col3 FROM tictactoe WHERE id = 3")
                col_pos = cur.fetchall()
                # print "Data", col_pos[0][0]
                if col_pos[0][0] == '9':
                    cur.execute("UPDATE tictactoe SET col3 = 'X' WHERE id = 3 ")
                    cur.execute("COMMIT")
                else:
                    print('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position already filled!!Please go back and select unfilled position representing a digit!!"</I></font>')

        else:
            print "NOne"
    print ('<br>')
    print ('<br>')
    cur.execute("SELECT col1,col2,col3 FROM tictactoe")
    #print (cur.fetchall())
    table_data = cur.fetchall()
    #print list(table_data)
    htmlcode = HTML.table(table_data)
    return table_data
    #chances = chances - 1


used_moves = []
#chances = 9
#while chances > 0:
player = form.getvalue('player_name')
pos = form.getvalue('move')
if player not in ("O" , "X"):
    print ('<form name="pyform" method="post" action="/cgi-bin/user_input.py"><br>')
    print ('<input type="submit" style="height:50px; width:175px; name="submit" value = Back>')
    print ('</form>')
    print ('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Please go back to the user input page and select a valid player (O or X)"</I></font></h3>')
 #   break
else:
    if pos not in ('1','2','3','4','5','6','7','8','9'):
        print ('<form name="pyform" method="post" action="/cgi-bin/user_input.py"><br>')
        print ('<input type="submit" style="height:50px; width:175px; name="submit" value = Back>')
        print ('</form>')
        print('<h2><br><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Please go back by clicking on back button and enter a valid position from 1 to 9 for the same player:"</I></font><br></h2>')
  #      break
    else:
        #print "USED_MOVES" , used_moves
        if pos not in used_moves:
            grid = table_entries(pos,player)
            used_moves.append(int(pos))
            print ('<h2><font face="Times New Roman" size = 5.5 color = "#08088A">"TicTacToe Player Positions are !!!!"</font></h2>')
            #print pos , used_moves
            print (HTML.table(grid))
            #print( owin(grid),xwin(grid),tie(grid))
            #print grid[1][0],grid[0][0] , grid[1][1] , grid[2][2]
            if owin(grid):
                print ('<h2>"Player O Wins!!"</h2>')
                print ('<h2>"GAME ENDS!!"</h2>')
                print ('<h2>"To start a new game, go back and click on TICTACTOE!</h2>')
                #break
            elif xwin(grid):
                print ('<h2>"Player X Wins!!"</h2>')
                print ('<h2>"GAME ENDS!!"</h2>')
                print ('<h2>"To start a new game, go back and click on TICTACTOE!</h2>')
            elif tie(grid):
                print ('<h2>"The game is a tie. None wins!!"</h2>')
                print ('<h2>"GAME ENDS!!"</h2>')
                print ('<h2>"To start a new game, go back and click on TICTACTOE!</h2>')

            print ('<form name="pyform" method="post" action="/cgi-bin/user_input.py"><br>')
            print ('<br>')
            print ('<input type="submit" style="height:50px; width:100px; name="submit" value = Back>')
            print ('</form>')
   #         break
            #cur.execute("COMMIT")

        else:
            print ('<h3><font face="Times New Roman" size = 5.5 color = "#08088A"><I>"Position(s) successfully filled. Please select an unfilled position representing digit to proceed further. Go back to input page by clicking on Back button."</I></font></h3>')
    #        break
#chances = chances - 1
db.close()
print ('</body>')
print ('</head>')
print ('</html>')
