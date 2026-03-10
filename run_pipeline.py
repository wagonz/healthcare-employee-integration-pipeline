import subprocess
import sys
import logging
from pathlib import Path

# Ensure logs folder exists
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_step(name, script):

    print(f"\nRunning step: {name}")
    logging.info(f"Starting step: {name}")

    result = subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        logging.error(f"Step failed: {name}")
        logging.error(result.stderr)

        print(f"Error in step: {name}")
        print(result.stderr)

        sys.exit(1)

    logging.info(result.stdout)
    print(result.stdout)


def main():

    print("\nStarting Healthcare Employee Data Pipeline")
    logging.info("Pipeline started")

    run_step("Validate CSV Data", "src/validate_data.py")
    run_step("Load CSV into Database", "src/load_to_db.py")
    run_step("Generate Department Report", "src/generate_report.py")
    run_step("Export JSON", "src/export_json.py")
    run_step("Export XML", "src/export_xml.py")

    print("\nPipeline completed successfully!")
    logging.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()