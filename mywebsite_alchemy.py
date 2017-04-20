from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Markup, send_from_directory, escape, session
import HTML , json
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app.config['MYSQL_DATABASE_USER'] = 'archena'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'myschema'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/webportal')
def webportal():
    return render_template('webportal.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    username = request.args.get('archena')
    password = request.args.get('1234')
    cursor = mysql.connect().cursor()
    #cursor.execute("CREATE TABLE littletots_signup (userid BIGINT UNIQUE , username varchar(45) NULL, email varchar(45) NULL, password varchar(45) NULL, PRIMARY KEY(userid))")
    #cursor.execute("COMMIT")
    error = None
    if request.method == 'POST':
        print "Hi"
        loginid = request.form.get('Name')
        email = request.form.get('Email')
        pwd = request.form.get('Password')
        print "loginid & pwd", loginid, pwd,email
        cursor.execute("SELECT count(userid) FROM littletots_signup")
        count = cursor.fetchone()[0]
        if int(count) > 0:
            cursor.execute('SELECT username FROM littletots_signup WHERE username = %s',(loginid,))
            names = cursor.fetchone()
            print loginid,names,count
            if names is None:
                userid = int(count) + 1
                print userid,loginid,email,pwd
                #cursor.execute("INSERT INTO littletots_signup VALUES(" +str(userid)+ "," +str(loginid)+ "," +str(email)+ ","+str(pwd)+")")
                cursor.execute('insert into littletots_signup values ("%s","%s","%s","%s")' % (userid, loginid, email,pwd))
                cursor.execute("COMMIT")
                cursor.execute("SELECT * FROM littletots_signup")
                print cursor.fetchall()
                msg = "Account created successfully! Please sign it to proceed"
                return render_template("signin.html", msg=msg)
                #return redirect((url_for('signin')))

            elif loginid in names:
                error = "Account exists. Please use a different account to signup"
                print "user id used"
        else:
            userid = int(count[0]) + 1
            print userid
            cursor.execute('INSERT INTO littletots_signup VALUES( %s%s%s%s', (userid, loginid, email, pwd,))
            cursor.execute("COMMIT")
            cursor.execute("SELECT * FROM littletots_signup")
            print cursor.fetchall()

            #return redirect((url_for('signin')))
            return render_template("signin.html", msg=msg)
    print ("login", request.form.get('Name'))
    print ("password", request.form.get('Password'))
    print ("email", request.form.get('Email'))
    print (request.method)
    return render_template("signup.html", error=error)

@app.route('/signin',methods=['GET', 'POST'])
def signin():
    eng = create_engine("mysql://archena:1234@localhost/myschema")
    #username = request.args.get('archena')
    #password = request.args.get('1234')
    #cursor = mysql.connect().cursor()
    # cursor.execute("CREATE TABLE littletots_signup (userid BIGINT UNIQUE , username varchar(45) NULL, email varchar(45) NULL, password varchar(45) NULL, PRIMARY KEY(userid))")
    # cursor.execute("COMMIT")
    with eng.connect() as cursor:
       # rs = cursor.execute(text('SELECT * FROM littletots_signup'))

        error = None
        if request.method == 'POST':
            print ("Signin")
            name = request.form.get('Name')
            pwd = request.form.get('Password')
            print ("Name & pwd", name, pwd)
            data = cursor.execute(text("SELECT username,password FROM littletots_signup "))
            #data = cursor.fetchall()
            data = [each for each in data]
            print data
            print tuple([name,pwd])
            if  tuple([name,pwd]) in data:
                print "Present"
                return redirect(url_for('student', student_par_name = name))
            else:
                msg = "Invalid User. Please try again."
                return render_template('signin.html' , msg=msg)
        return render_template('signin.html')

@app.route('/student/<student_par_name>')
def student(student_par_name):
    eng = create_engine("mysql://archena:1234@localhost/myschema")
    #username = request.args.get('archena')
    #password = request.args.get('1234')
    #cursor = mysql.connect().cursor()
    with eng.connect() as cursor:
        stu_name = cursor.execute('SELECT fname FROM littletots_student where lname = %s',student_par_name)
        stu_name = stu_name.fetchall()[0][0]
        print "Name" , stu_name
        cg = cursor.execute("select grade_name from littletots_assessment where skill = 'Cognitive' and student_name = %s ", stu_name)
        cognitive_grade = cg.fetchall()[0][0]
        #cognitive_grade = cursor.fetchall()[0][0]
        lg = cursor.execute("select grade_name from littletots_assessment where skill = 'Language' and student_name = %s",stu_name)
        Language_grade = lg.fetchall()[0][0]
        #Language_grade = cursor.fetchall()[0][0]
        se = cursor.execute('select grade_name from littletots_assessment where skill = "Self" and student_name = %s',stu_name)
        self_grade = se.fetchall()[0][0]
        #self_grade = cursor.fetchall()[0][0]
        soc = cursor.execute('select grade_name from littletots_assessment where skill = "Social Studies" and student_name = %s',stu_name)
        social_grade = soc.fetchall()[0][0]
        #social_grade = cursor.fetchall()[0][0]
        mg = cursor.execute('select grade_name from littletots_assessment where skill = "Math" and student_name = %s',stu_name)
        Math_grade = mg.fetchall()[0][0]
        #Math_grade = cursor.fetchall()[0][0]
        sg = cursor.execute('select grade_name from littletots_assessment where skill = "Science" and student_name = %s',stu_name)
        science_grade = sg.fetchall()[0][0]
        #science_grade = cursor.fetchall()[0][0]
        gmg = cursor.execute('select grade_name from littletots_assessment where skill = "Gross Motor" and student_name = %s',stu_name)
        grossmotor_grade = gmg.fetchall()[0][0]
        #grossmotor_grade = cursor.fetchall()[0][0]
        fmg = cursor.execute('select grade_name from littletots_assessment where skill = "Fine Motor" and student_name = %s',stu_name)
        finemotor_grade = fmg.fetchall()[0][0]
        #finemotor_grade = cursor.fetchall()[0][0]
        print "Grades",cognitive_grade,Language_grade,self_grade,social_grade,Math_grade,science_grade,grossmotor_grade,finemotor_grade
        return render_template('student.html',student_name = stu_name.upper(),name = student_par_name,cognitive = cognitive_grade,language = Language_grade,self1 = self_grade,social = social_grade,math = Math_grade,science = science_grade,gross = grossmotor_grade,fine = finemotor_grade)

@app.route('/results/<student_par_name>')
def results(student_par_name):
    eng = create_engine("mysql://archena:1234@localhost/myschema")
    #username = request.args.get('archena')
    #password = request.args.get('1234')
    #cursor = mysql.connect().cursor()
    with eng.connect() as cursor:
        fname = cursor.execute('SELECT fname FROM littletots_student where lname=%s', student_par_name)
        stu_name = fname.fetchall()
        print "student" , stu_name[0][0]
        cg = cursor.execute('select grade_name from littletots_assessment where skill = "Cognitive" and student_name = %s',stu_name[0][0])
        cognitive_grade = cg.fetchall()[0][0]
        lg = cursor.execute('select grade_name from littletots_assessment where skill = "Language" and student_name = %s',stu_name[0][0])
        Language_grade = lg.fetchall()[0][0]
        sg = cursor.execute('select grade_name from littletots_assessment where skill = "Self" and student_name = %s',stu_name[0][0])
        self_grade = sg.fetchall()[0][0]
        soc = cursor.execute('select grade_name from littletots_assessment where skill = "Social Studies" and student_name = %s',stu_name[0][0])
        social_grade = soc.fetchall()[0][0]
        ma = cursor.execute('select grade_name from littletots_assessment where skill = "Math" and student_name = %s',stu_name[0][0])
        Math_grade = ma.fetchall()[0][0]
        sg = cursor.execute('select grade_name from littletots_assessment where skill = "Science" and student_name = %s',stu_name[0][0])
        science_grade = sg.fetchall()[0][0]
        gg = cursor.execute('select grade_name from littletots_assessment where skill = "Gross Motor" and student_name = %s',stu_name[0][0])
        grossmotor_grade = gg.fetchall()[0][0]
        fg = cursor.execute('select grade_name from littletots_assessment where skill = "Fine Motor" and student_name = %s',stu_name[0][0])
        finemotor_grade = fg.fetchall()[0][0]
        print "Grades", cognitive_grade, Language_grade, self_grade, social_grade, Math_grade, science_grade, grossmotor_grade, finemotor_grade
        return render_template('results.html', student = stu_name[0][0].upper(), name =student_par_name, cognitive=cognitive_grade, language=Language_grade, self1=self_grade, social=social_grade, math=Math_grade, science=science_grade, gross=grossmotor_grade, fine=finemotor_grade)

@app.route('/signout')
def signout():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/teachers')
def teachers():
    return render_template('teachers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')


if __name__ == "__main__":
    app.run(debug=True)
