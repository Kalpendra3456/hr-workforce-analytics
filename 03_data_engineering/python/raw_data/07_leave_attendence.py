"""
===============================================================================
Project      : HR Workforce Analytics
File         : 07_leave_records.py
Purpose      : Generate realistic employee leave records
Author       : Kalpendra Yadav
===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

# =============================================================================
# Configuration
# =============================================================================

fake = Faker("en_IN")
random.seed(42)

NUM_RECORDS = 10000
NUM_EMPLOYEES = 3000

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 12, 31)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_FILE = BASE_DIR.parent / "raw_data" / "leave_records.csv"

print("Saving to:", OUTPUT_FILE)
print("Folder exists:", OUTPUT_FILE.parent.exists())# =============================================================================
# Master Data
# =============================================================================

LEAVE_TYPES = [
    "Annual Leave",
    "Sick Leave",
    "Casual Leave",
    "Emergency Leave",
    "Maternity Leave",
    "Paternity Leave",
    "Unpaid Leave"
]

LEAVE_REASONS = [
    "Vacation",
    "Medical Treatment",
    "Family Emergency",
    "Marriage",
    "Personal Work",
    "Religious Festival",
    "Child Care",
    "Higher Education"
]

APPROVAL_STATUS = [
    "Approved",
    "Pending",
    "Rejected"
]

APPROVAL_PROBABILITY = [
    0.88,
    0.08,
    0.04
]

# =============================================================================
# Generate Leave Records
# =============================================================================

records = []

for leave_id in range(1, NUM_RECORDS + 1):

    employee_id = random.randint(1, NUM_EMPLOYEES)

    leave_type = random.choice(LEAVE_TYPES)

    start_date = fake.date_between(
        start_date=START_DATE,
        end_date=END_DATE
    )

    total_leave_days = random.randint(1, 10)

    end_date = start_date + timedelta(days=total_leave_days - 1)

    approval_status = random.choices(
        APPROVAL_STATUS,
        weights=APPROVAL_PROBABILITY,
        k=1
    )[0]

    approved_by = fake.name() if approval_status == "Approved" else ""

    records.append({

        "leave_id": leave_id,
        "employee_id": employee_id,
        "leave_type": leave_type,
        "start_date": start_date,
        "end_date": end_date,
        "total_leave_days": total_leave_days,
        "leave_reason": random.choice(LEAVE_REASONS),
        "approval_status": approval_status,
        "approved_by": approved_by

    })

# =============================================================================
# Create DataFrame
# =============================================================================

leave_records = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

leave_records.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("Leave records generated successfully.")
print(f"Total Records : {len(leave_records):,}")
print(f"Employees     : {NUM_EMPLOYEES:,}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 70)