# Healthcare Employee Data Integration Pipeline

This project simulates a simplified enterprise HR data integration workflow similar to those used in systems like Workday or other HRIS platforms.

The pipeline loads employee data, stores it in a relational database, generates reports, and exports the data into multiple formats for integration with external systems.

## Why This Project Exists

This project was created to demonstrate core skills used in enterprise system integration roles such as Workday or HRIS platforms.

The pipeline demonstrates:

- ETL-style data processing
- SQL database operations
- Data format transformation (CSV → JSON/XML)
- REST API development
- Automated pipeline execution
- Logging and error handling

## Why This Project Exists

This project was created to demonstrate core skills used in enterprise system integration roles such as Workday or HRIS platforms.

The pipeline demonstrates:

- ETL-style data processing
- SQL database operations
- Data format transformation (CSV → JSON/XML)
- REST API development
- Automated pipeline execution
- Logging and error handling## Features

- Load employee data from CSV into SQLite
- Generate department summary reports
- Export employee data to JSON
- Export employee data to XML
- Provide API endpoints for employee data
- Automated pipeline execution
- Logging system for pipeline operations

- <img width="1470" height="956" alt="Screenshot 2026-03-08 at 3 45 50 PM" src="https://github.com/user-attachments/assets/60cf891c-c8d6-4e19-82bf-b99ca97caff5" />

## Technologies Used

- Python
- SQLite
- Flask
- CSV / JSON / XML
- REST API
- Logging

## Project Architecture
CSV Data -> Database -> Reports -> Data Exports -> API

## How to Run the Pipeline

Run the full pipeline: python3 run_pipeline.py
This will:
1. Load employee data into the database
2. Generate department report
3. Export JSON data
4. Export XML data
   
API endpoints:
/employees
/employees/active
/departments/report

## Purpose

This project demonstrates data integration, reporting, and API development skills commonly used in enterprise HR integration environments such as Workday.

## Future Improvements

- Automated scheduling
- Data validation
- Integration with external payroll API
- Docker containerization

