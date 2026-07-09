"""
===============================================================================
Project      : HR Workforce Analytics
File         : 12_promotions.py
Purpose      : Generate realistic employee promotion records
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

NUM_RECORDS = 2500
NUM_EMPLOYEES = 3000

# =============================================================================
# Output File
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR.parent / "raw_data"

OUTPUT_FILE = RAW_DATA_DIR / "promotions.csv"

# =============================================================================
# Master Data
# =============================================================================

OLD_DESIGNATIONS = [
    "Junior Executive",
    "Executive",
    "Senior Executive",
    "Analyst",
    "Senior Analyst",
    "Associate",
    "Assistant Manager"
]

NEW_DESIGNATIONS = [
    "Executive",
    "Senior Executive",
    "Lead Analyst",
    "Assistant Manager",
    "Manager",
    "Senior Manager",
    "Team Lead"
]

PROMOTION_REASON = [
    "Outstanding Performance",
    "Annual Promotion",
    "Leadership Development",
    "Role Expansion",
    "Business Requirement"
]

# =============================================================================
# Generate Promotion Records
# =============================================================================

records = []

for promotion_id in range(1, NUM_RECORDS + 1):

    old_designation = random.choice(OLD_DESIGNATIONS)
    new_designation = random.choice(NEW_DESIGNATIONS)

    while old_designation == new_designation:
        new_designation = random.choice(NEW_DESIGNATIONS)

    records.append({

        "promotion_id": promotion_id,
        "employee_id": random.randint(1, NUM_EMPLOYEES),
        "promotion_date": fake.date_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2025, 12, 31)
        ),
        "old_designation": old_designation,
        "new_designation": new_designation,
        "salary_increment_percent": round(random.uniform(8, 25), 2),
        "promotion_reason": random.choice(PROMOTION_REASON)

    })

# =============================================================================
# Create DataFrame
# =============================================================================

promotions = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

promotions.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("Promotion records generated successfully.")
print(f"Total Records : {len(promotions):,}")
print(f"Employees     : {NUM_EMPLOYEES:,}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 70)