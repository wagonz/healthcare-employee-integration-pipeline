import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
DB_PATH = "employees.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()
    employees = [dict(row) for row in rows]
    return jsonify(employees)

@app.route("/employees/active", methods=["GET"])
def get_active_employees():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM employees WHERE status = 'active'").fetchall()
    conn.close()
    employees = [dict(row) for row in rows]
    return jsonify(employees)

@app.route("/departments/report", methods=["GET"])
def get_departments_report():
    conn = get_db_connection()
    rows = conn.execute("""
        SELECT department, COUNT(*) as employee_count, AVG(salary) as average_salary
        FROM employees
        GROUP BY department
    """).fetchall()
    conn.close()
    report = [dict(row) for row in rows]
    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)