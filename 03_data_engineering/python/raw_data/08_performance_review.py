"""
===============================================================================
Project      : HR Workforce Analytics
File         : 08_performance_reviews.py
Purpose      : Generate realistic employee performance review data
Author       : Kalpendra Yadav
===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import random
from datetime import datetime

import pandas as pd
from faker import Faker

# =============================================================================
# Configuration
# =============================================================================

fake = Faker("en_IN")
random.seed(42)

NUM_RECORDS = 6000
NUM_EMPLOYEES = 3000

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR.parent / "raw_data"

OUTPUT_FILE = RAW_DATA_DIR / "performance_reviews.csv"
# =============================================================================
# Master Data
# =============================================================================

REVIEW_PERIODS = [
    "Q1",
    "Q2",
    "Q3",
    "Q4"
]

PERFORMANCE_CATEGORIES = [
    "Outstanding",
    "Exceeds Expectations",
    "Meets Expectations",
    "Needs Improvement",
    "Poor"
]

MANAGER_FEEDBACK = [
    "Excellent leadership and teamwork.",
    "Consistently exceeds expectations.",
    "Reliable and dependable employee.",
    "Good communication and collaboration.",
    "Strong technical skills.",
    "Needs improvement in productivity.",
    "Requires additional coaching.",
    "Demonstrates strong problem-solving skills."
]

# =============================================================================
# Generate Performance Reviews
# =============================================================================

records = []

for review_id in range(1, NUM_RECORDS + 1):

    employee_id = random.randint(1, NUM_EMPLOYEES)

    rating = round(random.uniform(2.0, 5.0), 1)

    if rating >= 4.5:
        category = "Outstanding"
    elif rating >= 4.0:
        category = "Exceeds Expectations"
    elif rating >= 3.0:
        category = "Meets Expectations"
    elif rating >= 2.5:
        category = "Needs Improvement"
    else:
        category = "Poor"

    records.append({

        "review_id": review_id,
        "employee_id": employee_id,
        "review_date": fake.date_between(
            start_date=datetime(2024,1,1),
            end_date=datetime(2025,12,31)
        ),
        "review_period": random.choice(REVIEW_PERIODS),
        "performance_rating": rating,
        "performance_category": category,
        "goals_completed": random.randint(3,10),
        "manager_feedback": random.choice(MANAGER_FEEDBACK),
        "promotion_recommended": random.choice(["Yes","No"])

    })

# =============================================================================
# Create DataFrame
# =============================================================================

performance_reviews = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

performance_reviews.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("="*70)
print("Performance Review data generated successfully.")
print(f"Total Records : {len(performance_reviews):,}")
print(f"Employees     : {NUM_EMPLOYEES:,}")
print(f"Output File   : {OUTPUT_FILE}")
print("="*70)