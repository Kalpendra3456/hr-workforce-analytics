"""
===============================================================================
Project      : HR Workforce Analytics
File         : 09_salary_history.py
Purpose      : Generate realistic employee salary history data
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

NUM_RECORDS = 7000
NUM_EMPLOYEES = 3000

# =============================================================================
# Output File
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR.parent / "raw_data"

OUTPUT_FILE = RAW_DATA_DIR / "salary_history.csv"

# =============================================================================
# Master Data
# =============================================================================

SALARY_CHANGE_REASON = [
    "Annual Increment",
    "Promotion",
    "Market Adjustment",
    "Performance Bonus",
    "Salary Revision"
]

# =============================================================================
# Generate Salary History
# =============================================================================

records = []

for salary_id in range(1, NUM_RECORDS + 1):

    employee_id = random.randint(1, NUM_EMPLOYEES)

    previous_salary = random.randint(250000, 1800000)

    increment_percent = round(random.uniform(3, 20), 2)

    new_salary = round(
        previous_salary * (1 + increment_percent / 100),
        2
    )

    records.append({

        "salary_id": salary_id,
        "employee_id": employee_id,
        "effective_date": fake.date_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2025, 12, 31)
        ),
        "previous_salary": previous_salary,
        "new_salary": new_salary,
        "increment_percent": increment_percent,
        "change_reason": random.choice(SALARY_CHANGE_REASON)

    })

# =============================================================================
# Create DataFrame
# =============================================================================

salary_history = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

salary_history.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("Salary History generated successfully.")
print(f"Total Records : {len(salary_history):,}")
print(f"Employees     : {NUM_EMPLOYEES:,}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 70)