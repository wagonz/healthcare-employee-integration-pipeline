import csv
import sqlite3
from pathlib import Path

DB_PATH = "employees.db"
CSV_PATH = "data/employees.csv"

def main():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT,
            hire_date TEXT,
            job_id TEXT,
            salary REAL,
            manager_id INTEGER,
            department TEXT,
            status TEXT
        )
    ''')

    # Read the CSV file and insert data into the employees table
    with open(CSV_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
                INSERT OR REPLACE INTO employees (
    employee_id, first_name, last_name, email, phone_number,
    hire_date, job_id, salary, manager_id, department, status
) VALUES (
    :employee_id, :first_name, :last_name, :email, :phone_number,
    :hire_date, :job_id, :salary, :manager_id, :department, :status
)
            ''', row)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    print("Employees data has been successfully loaded into the database.")
 
 #end main   
if __name__ == "__main__":
    main()
    
