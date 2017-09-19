import pymysql
from flask import Flask,render_template,redirect,url_for,request



App = Flask(__name__)
db = pymysql.connect("localhost","root","66165107","db")
cursor = db.cursor()

#sql = """CREATE TABLE USUARIO(ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, NOMBRE VARCHAR(20) NOT NULL,APELLIDO VARCHAR(20),EDAD VARCHAR(2),SEXO CHAR (1))"""
#
#cursor.execute(sql)
#db.close()

@App.route('/')
def index():
    return render_template('index.html')

@App.route('/todo',methods=['POST','GET'])
def mostrar_todo():
    if request.method == 'POST':
        nom = request.form['nom']
        ape = request.form['ape']
        edad = request.form['edad']
        sex = request.form['sex']

        sql = """INSERT INTO USUARIO(NOMBRE,APELLIDO,EDAD,SEXO)
                    VALUES('%s','%s','%s','%s')""" % (nom,ape,edad,sex)

        try:
            print(sql)
            cursor.execute(sql)
            db.commit()
            #db.close()
        except Exception as e:
            print(e)
            db.rollback()
        return redirect(url_for('index'))
    return render_template('todo.html')


@App.route('/borrar', methods=['POST','GET'])
def borrar():
    if request.method == 'POST':
        nom = request.form['nom']
        ape = request.form['ape']
        sql = "DELETE FROM USUARIO WHERE NOMBRE = '%s' and APELLIDO = '%s'" % (nom,ape)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        return redirect(url_for('index'))
    return render_template('borrar.html')

if __name__ == '__main__':
    sql = """CREATE TABLE USUARIO(ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,NOMBRE VARCHAR(20) NOT NULL,APELLIDO VARCHAR(20),EDAD VARCHAR(2),SEXO CHAR (1))"""
    App.run()
    db.close()