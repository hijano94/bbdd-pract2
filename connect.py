import os
import cx_Oracle
from flask import Flask, render_template
	
db_user = os.environ.get('DBAAS_USER_NAME', 'carlos')
db_password = os.environ.get('DBAAS_USER_PASSWORD', '1234')
db_connect = os.environ.get('DBAAS_DEFAULT_CONNECT_DESCRIPTOR', 	"192.168.1.24:1521/ORCL")
service_port = port=os.environ.get('PORT', '8080')

app = Flask(__name__)

@app.route('/')
def index():
    connection = cx_Oracle.connect(db_user, db_password, db_connect)
    cur = connection.cursor()
    cur.execute(‘select * from jockeys‘)
    col = cur.fetchall()
    render_template(‘plantilla.html’,col=col)
    cur.close()
    connection.close()
		
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= int(service_port) )