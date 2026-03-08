import json
import sqlite3

DB_PATH = "employees.db"
JSON_PATH = "data/employees.json"

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Query all employees
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Convert rows to list of dictionaries
    employees = [dict(zip(column_names, row)) for row in rows]

    # Write to JSON file
    with open(JSON_PATH, "w") as jsonfile:
        json.dump(employees, jsonfile, indent=4)

    # Close the connection
    conn.close()
    print("Employees data has been successfully exported to JSON.")

if __name__ == "__main__":
    main()