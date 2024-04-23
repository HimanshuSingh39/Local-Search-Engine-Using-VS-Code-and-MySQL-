import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12qw!@QW",
            database="dcc_a4"
        )
        return db_connection
    except mysql.connector.Error as err:
        print("Error connecting to the database:", err)
        return None
        
def execute_query(db_connection, query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print("Error executing query:", err)
        return None

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    column = request.args.get('column')
    db_connection = connect_to_database()
    if not db_connection:
        return "Error connecting to the database"
    search_results = execute_query(db_connection, f"SELECT * FROM csv1 WHERE `{column.replace('_',' ')}` LIKE '%{query}%'")
    print(search_results)  # Print search results for debugging
    db_connection.close()

 
    return render_template("search.html", query=query, column=column, results=search_results)

@app.route('/search2', methods=['GET'])
def search2():
    query = request.args.get('query')
    column = request.args.get('column')
    
    db_connection = connect_to_database()
    if not db_connection:
        return "Error connecting to the database"

   
    search_results = execute_query(db_connection, f"SELECT * FROM csv2 WHERE `{column.replace('_',' ')}` LIKE '%{query}%'")
    print(search_results)  # Print search results for debugging

    db_connection.close()
    return render_template("search2.html", query=query, column=column, results=search_results)

if __name__ == "__main__":
    app.run(debug=True, port=8900)
