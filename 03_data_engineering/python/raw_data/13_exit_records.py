"""
===============================================================================
Project      : HR Workforce Analytics
File         : 13_exit_records.py
Purpose      : Generate realistic employee exit records
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

NUM_RECORDS = 750
NUM_EMPLOYEES = 3000

# =============================================================================
# Output File
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR.parent / "raw_data"

OUTPUT_FILE = RAW_DATA_DIR / "exit_records.csv"

# =============================================================================
# Master Data
# =============================================================================

EXIT_TYPES = [
    "Resignation",
    "Termination",
    "Retirement",
    "Contract End"
]

EXIT_REASONS = [
    "Better Career Opportunity",
    "Higher Education",
    "Relocation",
    "Retirement",
    "Performance Issues",
    "Personal Reasons",
    "Health Issues",
    "Company Restructuring",
    "End of Contract"
]

ELIGIBLE_FOR_REHIRE = [
    "Yes",
    "No"
]

# =============================================================================
# Generate Exit Records
# =============================================================================

records = []

for exit_id in range(1, NUM_RECORDS + 1):

    exit_type = random.choices(
        EXIT_TYPES,
        weights=[70, 15, 10, 5],
        k=1
    )[0]

    records.append({

        "exit_id": exit_id,
        "employee_id": random.randint(1, NUM_EMPLOYEES),
        "exit_date": fake.date_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2025, 12, 31)
        ),
        "exit_type": exit_type,
        "exit_reason": random.choice(EXIT_REASONS),
        "notice_period_days": random.choice([0, 15, 30, 60, 90]),
        "eligible_for_rehire": random.choices(
            ELIGIBLE_FOR_REHIRE,
            weights=[80, 20],
            k=1
        )[0]

    })

# =============================================================================
# Create DataFrame
# =============================================================================

exit_records = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

exit_records.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("Exit Records generated successfully.")
print(f"Total Records : {len(exit_records):,}")
print(f"Employees     : {NUM_EMPLOYEES:,}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 70)