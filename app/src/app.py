from flask import Flask,request
import os
import json
import pyodbc
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    #hostname = os.uname()[1]
    return 'Hello World - '

@app.route('/database')
def db_data():
    try:
        AZURE_SQL_CONNECTION="Driver={ODBC Driver 18 for SQL Server};Server=tcp:appaccount2306.database.windows.net,1433;Database=appaccount2306;Uid=admin123;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
        
        AZURE_SQL_CONNECTION = AZURE_SQL_CONNECTION.replace('{your_password_here}','admin@123')
        try:
            conn=pyodbc.connect(AZURE_SQL_CONNECTION)
        except Exception as e:
            print(str(e))
        if request.args.get("id"):
            sql_query="select * from Employee where EmployeeID="+request.args.get("id")
        else:
            sql_query="select * from Employee"

        cursor=conn.cursor()

        cursor.execute(sql_query)
        data=[]
        for row1 in cursor.fetchall():
            formatted_text="{'EmployeeID': '"+str(row1[0])+"','EmpName':'"+str(row1[1])+"', 'DeptName':'"+str(row1[2])+"'}"
            data.append(json.dumps(formatted_text))
        
        return data
    except Exception as e:
        return str(e)


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()