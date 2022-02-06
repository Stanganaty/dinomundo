from flask import Flask, request, jsonify
from flask_mysqldb import MYSQL
from flask import jsonify
from flask_cors import CORS, cross_origin

app= Flask(_name_)

cors= CORS(app,resources={r"/*": {"origins": "*"}})

app.confing ['MYSQL_HOST']='localhost'
app.confing ['MYSQL_USER']= 'root'
app.confing ['MYSQL_PASSWORD']= 'fullstack'
app.confing  ['MYSQL_DB']= 'contactost'
mysql= MYSQL(app)

@app.route('nuevo'methods== ['POST'])
@cross_origin():
def nuevo():
	if request.methods== 'POST':
	request_data= request.get_json()
    nombre y apellido = request_data ['nombre y apellido']
    correo = request_data ['correo']
    edad =request_data ['edad']
    cur= mysql.connection.cursor ()
    cur.execute ('INSERT INTO mensajes (nombre y apellido, correo, edad) VALUES ($s,$s,$s)
    mysql.connection.commit
    return "GUARDADO OK"
    
    
    
 if_name_== '_main_':
	 app.run (host='0.0.0.0',port= 4003
