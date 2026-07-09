"""
===============================================================================
Project      : HR Workforce Analytics
File         : 11_training_records.py
Purpose      : Generate realistic employee training records
Author       : Kalpendra Yadav
===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import random
from pathlib import Path
from datetime import datetime

import pandas as pd
from faker import Faker

# =============================================================================
# Configuration
# =============================================================================

fake = Faker("en_IN")
random.seed(42)

NUM_RECORDS = 8000
NUM_EMPLOYEES = 3000
NUM_PROGRAMS = 100

# =============================================================================
# Output File
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR.parent / "raw_data"

OUTPUT_FILE = RAW_DATA_DIR / "training_records.csv"

# =============================================================================
# Master Data
# =============================================================================

COMPLETION_STATUS = [
    "Completed",
    "In Progress",
    "Not Completed"
]

CERTIFICATION_STATUS = [
    "Yes",
    "No"
]

# =============================================================================
# Generate Training Records
# =============================================================================

records = []

for training_id in range(1, NUM_RECORDS + 1):

    completion = random.choices(
        COMPLETION_STATUS,
        weights=[80, 15, 5],
        k=1
    )[0]

    score = random.randint(60, 100) if completion == "Completed" else None

    certification = (
        "Yes"
        if completion == "Completed" and score >= 75
        else "No"
    )

    records.append({

        "training_id": training_id,
        "employee_id": random.randint(1, NUM_EMPLOYEES),
        "program_id": random.randint(1, NUM_PROGRAMS),
        "training_date": fake.date_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2025, 12, 31)
        ),
        "completion_status": completion,
        "score": score,
        "certification_status": certification

    })

# =============================================================================
# Create DataFrame
# =============================================================================

training_records = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

training_records.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("Training Records generated successfully.")
print(f"Total Records : {len(training_records):,}")
print(f"Employees     : {NUM_EMPLOYEES:,}")
print(f"Programs      : {NUM_PROGRAMS}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 70)