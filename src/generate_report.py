import csv
import sqlite3

DB_PATH = "employees.db"
REPORT_PATH = "data/employee_report.csv"

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Query all employees
    cursor.execute("""
        SELECT department, COUNT(*) as employee_count 
        FROM employees 
        GROUP BY department 
        ORDER BY employee_count DESC, department ASC
    """)
    rows = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Write to CSV file
    with open(REPORT_PATH, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(zip(column_names, row)))

    # Close the connection
    conn.close()
    print("Employee report has been successfully generated in CSV format.")

if __name__ == "__main__":
    main()