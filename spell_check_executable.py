#!c:/Python27/python.exe

print ("Content-type: text/html\r\n\r\n")
print ('<html>')
print ('<head>')
import cgi, cgitb
import random

cgitb.enable()  # for debugging
form = cgi.FieldStorage()
import re
sentence = form.getvalue('lines_of_text')
words = sentence.split(" ")
#pat = re.compile(r'\b[a-zA-Z]')
new_words = []
for each_word in words:
    if not each_word.isalpha():
    #re.sub(r'[?]' , " " , each_word)
        each_word = re.sub(r'[\?!\.\']' , "" , each_word)
        #print each_word
        new_words.append(each_word)
    else:
        new_words.append(each_word)
#print new_words
dictionary = {}
with open("DictionaryE.txt")as fname:
    lines = fname.readlines()
    #print type(lines)
    for i in range(int(len(lines))):
        dictionary[i] = lines[i].strip("\n")

wrong = []
for every_word in new_words:
    if every_word.lower() not in dictionary.values():
        wrong.append(every_word)
print("Incorrect words are:")
for i in wrong:
    print (i)
    print('<br>')

print ('</body>')
print('</html>')
