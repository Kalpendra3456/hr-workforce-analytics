"""
===============================================================================
Project      : HR Workforce Analytics
File         : 10_training_programs.py
Purpose      : Generate realistic employee training programs
Author       : Kalpendra Yadav
===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import random
from pathlib import Path

import pandas as pd
from faker import Faker

# =============================================================================
# Configuration
# =============================================================================

fake = Faker("en_IN")
random.seed(42)

NUM_PROGRAMS = 100

# =============================================================================
# Output File
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR.parent / "raw_data"

OUTPUT_FILE = RAW_DATA_DIR / "training_programs.csv"

# =============================================================================
# Master Data
# =============================================================================

PROGRAM_NAMES = [
    "Leadership Development",
    "Advanced Excel",
    "Power BI Fundamentals",
    "SQL for Business",
    "Python Programming",
    "Communication Skills",
    "Project Management",
    "Cyber Security Awareness",
    "Time Management",
    "Data Analytics",
    "Customer Service",
    "Financial Analysis",
    "Machine Learning Basics",
    "Cloud Computing",
    "Business Intelligence",
    "Workplace Ethics",
    "Sales Excellence",
    "Digital Marketing",
    "Conflict Resolution",
    "Risk Management"
]

TRAINERS = [
    "Internal Trainer",
    "External Consultant",
    "Microsoft",
    "Google",
    "IBM",
    "Oracle",
    "Udemy Business",
    "Coursera"
]

TRAINING_TYPES = [
    "Technical",
    "Soft Skills",
    "Compliance",
    "Leadership"
]

DELIVERY_MODE = [
    "Online",
    "Offline",
    "Hybrid"
]

# =============================================================================
# Generate Training Programs
# =============================================================================

records = []

for program_id in range(1, NUM_PROGRAMS + 1):

    records.append({

        "program_id": program_id,
        "program_name": random.choice(PROGRAM_NAMES),
        "training_type": random.choice(TRAINING_TYPES),
        "trainer": random.choice(TRAINERS),
        "duration_hours": random.choice([4, 8, 12, 16, 24, 40]),
        "delivery_mode": random.choice(DELIVERY_MODE),
        "cost_per_employee": random.randint(1000, 25000)

    })

# =============================================================================
# Create DataFrame
# =============================================================================

training_programs = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

training_programs.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("Training Programs generated successfully.")
print(f"Programs      : {len(training_programs):,}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 70)