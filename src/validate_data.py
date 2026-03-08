import csv
import re
import sys

CSV_PATH = "data/employees.csv"

email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")

def validate_row(row, line_number):
    
    errors = []
    
    if not row.get("employee_id"):
        errors.append(f"Line {line_number}: Missing employee_id")
    
    if not row.get("first_name"):
        errors.append(f"Line {line_number}: Missing first_name")
        
    if not row.get("last_name"):
        errors.append(f"Line {line_number}: Missing last_name")
    
    email = row.get("email")
    
    if not email or not email_pattern.match(email):
        errors.append(f"Line {line_number}: Invalid email format")
        
    return errors

def main():
    print("Validating employee data...")
    
    seen_ids = set()
    error_count = 0
    
    with open(CSV_PATH) as file:
        reader = csv.DictReader(file)
        
        for line_number, row in enumerate(reader, start=2):
            errors = validate_row(row, line_number)
            
            emp_id = row.get("employee_id")
            if emp_id in seen_ids:
                errors.append(f"Line {line_number}: Duplicate employee_id")
            
            seen_ids.add(emp_id)
            
            if errors:
                error_count += 1
                print(f"Line {line_number}: {', '.join(errors)}")
    
    if error_count > 0:
        print(f"\nValidation failed with {error_count} errors.")
        sys.exit(1)
    
    print("Validation successful.")
    
if __name__ =="__main__":
    main()
        
    
                    