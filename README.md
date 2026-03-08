# Healthcare Employee Data Integration Pipeline

This project simulates a simplified enterprise HR data integration workflow similar to those used in systems like Workday or other HRIS platforms.

The pipeline loads employee data, stores it in a relational database, generates reports, and exports the data into multiple formats for integration with external systems.

## Features

- Load employee data from CSV into SQLite
- Generate department summary reports
- Export employee data to JSON
- Export employee data to XML
- Provide API endpoints for employee data
- Automated pipeline execution
- Logging system for pipeline operations

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

