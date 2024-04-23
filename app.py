import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Connect to the MySQL database
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

# Execute SQL query based on user input
def execute_query(db_connection, query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print("Error executing query:", err)
        return None

# Route for the main page
@app.route('/')
def main_page():
    return render_template("index.html")

# Route for handling search queries for csv1
@app.route('/search', methods=['GET'])
def search():
    # Retrieve query parameters from the request
    query = request.args.get('query')
    column = request.args.get('column')
    
    # Connect to the database
    db_connection = connect_to_database()
    if not db_connection:
        return "Error connecting to the database"

    # Execute database search based on the query and column
    search_results = execute_query(db_connection, f"SELECT * FROM csv1 WHERE `{column.replace('_',' ')}` LIKE '%{query}%'")
    print(search_results)  # Print search results for debugging
    
    # Close database connection
    db_connection.close()

    # Pass search results to the template
    return render_template("search.html", query=query, column=column, results=search_results)

# Route for handling search queries for csv2
@app.route('/search2', methods=['GET'])
def search2():
    query = request.args.get('query')
    column = request.args.get('column')
    
    # Connect to the database
    db_connection = connect_to_database()
    if not db_connection:
        return "Error connecting to the database"

    # Execute database search based on the query and column
    search_results = execute_query(db_connection, f"SELECT * FROM csv2 WHERE `{column.replace('_',' ')}` LIKE '%{query}%'")
    print(search_results)  # Print search results for debugging

    db_connection.close()
    return render_template("search2.html", query=query, column=column, results=search_results)

if __name__ == "__main__":
    app.run(debug=True, port=8900)
