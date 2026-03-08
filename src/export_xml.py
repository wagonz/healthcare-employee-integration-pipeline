import sqlite3
import xml.etree.ElementTree as ET

DB_PATH = "employees.db"
XML_PATH = "data/employees.xml"

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Query all employees
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Create the root element
    root = ET.Element("employees")

    # Convert rows to XML elements
    for row in rows:
        employee = ET.SubElement(root, "employee")
        for col_name, value in zip(column_names, row):
            child = ET.SubElement(employee, col_name)
            child.text = str(value)

    # Write to XML file
    tree = ET.ElementTree(root)
    tree.write(XML_PATH, encoding="utf-8", xml_declaration=True)

    # Close the connection
    conn.close()
    print("Employees data has been successfully exported to XML.")

if __name__ == "__main__":
    main()