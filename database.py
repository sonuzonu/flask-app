import mysql.connector


def get_data():
    mydb = mysql.connector.connect(host ="localhost",user = "root",password = "sonu",database ="testdb")
    mycursor = mydb.cursor()
    mycursor.exwcute("SELECT * FROM employee")
    result = mycursor.fetchmany()
    mycursor.close()
    mydb.close()
    return result                       