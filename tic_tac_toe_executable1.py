#!c:/Python27/python.exe

print ("Content-type: text/html\r\n\r\n")
print ('<html>')
print ('<body>')
import cgi,cgitb
import random
cgitb.enable() #for debugging  
form = cgi.FieldStorage()  
player1 = form.getvalue('First')
print ('<h4>')
print ("The first player's name is {}:" .format(player1))
print ('</h4>')
player2 = form.getvalue('Second')
print ('<h4>')
print ("The second player's name is {}:" .format(player2))
print ('</h4>')
print ('<br>')
print ('<h2> "TIC-TAC-TOE" </h2>')
import HTML
#print "hello"
a = [1,2,3,4,5,6,7,8,9]
board = [
        ['1',   '2',   '3'],
        ['4',   '5',   '6'],
        ['7',   '8',   '9'],
        ]
htmlcode = HTML.table(board)
#print HTML.TableRow
#print HTML.TableCell
#print htmlcode
#htmlcode = HTML.table(board)
#print htmlcode

cell = [str(i) for i in range(9)]
#board = cell[0] + "\t" + cell[1] + "\t" + cell[2] +"\n" + cell[3] + "\t" + cell[4] + "\t" + cell[5] + "\n" + cell[6] + "\t" + cell[7] + "\t" + cell[8]

def board_positions(move):
    #print move , cell[move -1]
    board[0][0] = cell[0]
    board[0][1] = cell[1]
    board[0][2] = cell[2]
    board[1][0] = cell[3]
    board[1][1] = cell[4]
    board[1][2] = cell[5]
    board[2][0] = cell[6]
    board[2][1] = cell[7]
    board[2][2] = cell[8]

    return  board

#print (board)

def owin():
    if board[0][0] == board[0][1] == board[0][2] == 'O' or board[1][0] == board[1][1] == board[1][2] == 'O' or board[2][0] == board[2][1] == board[2][2] == 'O' or board[0][0] == board[1][0] == board[2][0] == 'O' or board[0][1] == board[1][1] == board[2][1] == 'O' or board[0][2] == board[1][2] == board[2][2] == 'O':
        return True
    else:
        return False
def xwin():
    if board[0][0] == board[0][1] == board[0][2] == 'X' or board[1][0] == board[1][1] == board[1][2] == 'X' or board[2][0] == board[2][1] == board[2][2] == 'X' or board[0][0] == board[1][0] == board[2][0] == 'X' or board[0][1] == board[1][1] == board[2][1] == 'X' or board[0][2] == board[1][2] == board[2][2] == 'X':
        return True
    else:
        return False
def tie():
    if board[0][0] in ('O', 'X') and board[0][1] in ('O', 'X') and board[0][2] in ('O', 'X') and board[1][0] in ('O', 'X') and board[1][1] in ('O', 'X') and board[1][2] in ('O', 'X') and board[2][0] in ('O', 'X') and board[2][1] in ('O', 'X') and board[2][2] in ('O', 'X'):
        return True
    else:
        return False

chances = 9
#player1 = raw_input("Enter the name of the first player: ")
#player2 = raw_input("Enter the name of the second player: ")
#print ("First player's name is {}" .format(player1))
#print ("Second player's name is {}" .format(player2))
cell[0] = board[0][0]
cell[1] = board[0][1]
cell[2] = board[0][2]
cell[3] = board[1][0]
cell[4] = board[1][1]
cell[5] = board[1][2]
cell[6] = board[2][0]
cell[7] = board[2][1]
cell[8] = board[2][2]
next_player = player1
while chances > 0:
    if next_player == player1:
        #print ('<br><br>')
        print ('<h3>"First Player\'s turn"</h3>')
        #print ('<br><br>')
        print ('<h3>"Place your move in any place from 1 to 9: "</h3>')
        move = random.choice(a)
        print ('<br>')
        print ('<h3>')
        print ("O placed in position : " , move)
        print ('</h3>')
        if move > 0 and move < 10:
            if cell[int(move) - 1] not in ["O" , "X"]:
                cell[int(move) -1] = "O"
                board = board_positions(move)
                #board = cell[0] + "\t" + cell[1] + "\t" + cell[2] + "\n" + cell[3] + "\t" + cell[4] + "\t" + cell[5] + "\n" + cell[6] + "\t" + cell[7] + "\t" + cell[8]
                htmlcode = HTML.Table(board)
                print (htmlcode)
                if owin():
                 #   print ('<br><br>')
                    print ('<h3>')
                    print ("Player1 {} wins!!".format(player1))
                    print ('</h3>')
                    break
                elif tie():
                    print ('<h3>')
                    print ("None wins!! It is a tie!")
                    print ('</h3>')
                    break
                next_player = player2
                chances = chances - 1
            else:
                #print ('<br><br>')
                print ('<h3>"Position already filled. Please select an unfilled position!!"</h3>')
                move = random.choice(a)
        else:
            print ('<br><br>')
            print("Enter position from 1 to 9")
    else:
        #print ('<br><br>')
        print ('<h3>"Second Player\'s turn"</h3>')
        #print ('<br><br>')
        #print ('<br>')
        print ('<h3>"Place your move in any place from 1 to 9: "</h3>')
        move = random.choice(a)
        print ('<h3>')
        print ("X placed in position : ", move)
        print ('</h3>')

        if move > 0 and move < 10:
            if cell[int(move) - 1] not in ["O", "X"]:
                cell[int(move) - 1] = "X"
                board = board_positions(move)
                #board = cell[0] + "\t" + cell[1] + "\t" + cell[2] + "\n" + cell[3] + "\t" + cell[4] + "\t" + cell[5] + "\n" + cell[6] + "\t" + cell[7] + "\t" + cell[8]
                htmlcode = HTML.Table(board)
                print (htmlcode)

                if xwin():
                    #print ('<br><br>')
                    print ('<h3>')
                    print ("Player2 {} wins!!".format(player2))
                    print ('</h3>')
                    break
                elif tie():
                    print ('<h3>')
                    print ("None wins!! It is a tie!")
                    print ('</h3>')
                    break
                next_player = player1
                chances = chances - 1
            else:
                #print ('<br><br>')
                print ('<h3>"Position already filled. Please select an unfilled position!!"</h3>')
                move = random.choice(a)
        else:
            print ('<br><br>')
            print("Enter position from 1 to 9")


print ('</body>')
print ('</html>')
