# Healthcare Employee Data Integration Pipeline

This project simulates a simplified enterprise HR data integration workflow similar to those used in systems such as Workday or other HRIS platforms.

The pipeline loads employee data, validates the data, stores it in a relational database, generates reports, and exports the data into multiple formats for integration with external systems.

## Features

- CSV data ingestion
- Data validation before database loading
- SQLite relational database storage
- Department summary report generation
- Data export to JSON and XML formats
- REST API endpoints using Flask
- Automated pipeline execution
- Logging of pipeline operations

## Project Architecture

'''
employees.csv
      │
      ▼
validate_data.py
      │
      ▼
load_to_db.py
      │
      ▼
SQLite Database
      │
 ┌────┴───────────────┐
 ▼                    ▼
generate_report.py   export_json.py
 │                    │
 ▼                    ▼
department_report    employees.json
      │
      ▼
export_xml.py
      │
      ▼
employees.xml
      │
      ▼
Flask API
```

## Project Structure

```
healthcare-employee-integration-pipeline
│
├── src
│   ├── validate_data.py
│   ├── load_to_db.py
│   ├── generate_report.py
│   ├── export_json.py
│   ├── export_xml.py
│   └── api.py
│
├── data
│   └── employees.csv
│
├── logs
│
├── output
│
├── run_pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

Python 3

Install dependencies:

```
pip install -r requirements.txt
```

## Running the Full Pipeline

Run the automated pipeline:

```
python3 run_pipeline.py
```

The pipeline will perform the following steps:

1. Validate CSV data
2. Load employee data into the SQLite database
3. Generate department summary report
4. Export employee data to JSON
5. Export employee data to XML

## Running the API

Start the API server:

```
python3 src/api.py
```

Available endpoints:

```
/employees
/employees/active
/departments/report
```

## Example Pipeline Output

```
Starting Healthcare Employee Data Pipeline

Running step: Validate CSV Data
Validation successful

Running step: Load CSV into Database
Employees data loaded successfully

Running step: Generate Department Report
Report generated

Running step: Export JSON
Export completed

Running step: Export XML
Export completed

Pipeline completed successfully
```

## Logging

Pipeline activity is logged to:

```
logs/pipeline.log
```

This log records pipeline steps, errors, and execution timestamps.

## Purpose

This project demonstrates core skills used in enterprise integration and HRIS environments:

- ETL-style data processing
- SQL database operations
- Data format transformation (CSV → JSON/XML)
- REST API development
- Automated pipeline execution
- Logging and error handling

## Author
Wascar Gonzalez  
GitHub: https://github.com/wagonz





