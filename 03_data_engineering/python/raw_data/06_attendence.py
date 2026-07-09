"""
===============================================================================
Project      : HR Workforce Analytics
File         : 06_attendance.py
Purpose      : Generate realistic employee attendance data
Author       : Kalpendra Yadav
===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import random
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

# =============================================================================
# Configuration
# =============================================================================

random.seed(42)
np.random.seed(42)

NUM_EMPLOYEES = 3000

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

# =============================================================================
# Output File
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR.parent / "raw_data" / "attendance.csv"

# =============================================================================
# Attendance Status
# =============================================================================

ATTENDANCE_STATUS = [
    "Present",
    "Absent",
    "Work From Home",
    "Paid Leave",
    "Sick Leave"
]

ATTENDANCE_PROBABILITY = [
    0.82,
    0.05,
    0.05,
    0.04,
    0.04
]

# =============================================================================
# Generate Attendance Data
# =============================================================================

records = []

attendance_id = 1
current_date = START_DATE

while current_date <= END_DATE:

    # Monday-Friday only
    if current_date.weekday() < 5:

        for employee_id in range(1, NUM_EMPLOYEES + 1):

            status = np.random.choice(
                ATTENDANCE_STATUS,
                p=ATTENDANCE_PROBABILITY
            )

            check_in = None
            check_out = None
            working_hours = 0
            overtime_hours = 0

            if status in ["Present", "Work From Home"]:

                check_in = datetime(
                    current_date.year,
                    current_date.month,
                    current_date.day,
                    random.randint(8, 10),
                    random.randint(0, 59)
                )

                working_hours = random.randint(8, 10)

                check_out = check_in + timedelta(hours=working_hours)

                overtime_hours = max(0, working_hours - 8)

            records.append({

                "attendance_id": attendance_id,
                "employee_id": employee_id,
                "attendance_date": current_date.strftime("%Y-%m-%d"),
                "status": status,
                "check_in": check_in.strftime("%H:%M:%S") if check_in else "",
                "check_out": check_out.strftime("%H:%M:%S") if check_out else "",
                "working_hours": working_hours,
                "overtime_hours": overtime_hours

            })

            attendance_id += 1

    current_date += timedelta(days=1)

# =============================================================================
# Create DataFrame
# =============================================================================

attendance = pd.DataFrame(records)

# =============================================================================
# Export CSV
# =============================================================================

attendance.to_csv(OUTPUT_FILE, index=False)

# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("HR WORKFORCE ANALYTICS")
print("=" * 70)
print("Attendance data generated successfully.")
print(f"Employees      : {NUM_EMPLOYEES:,}")
print(f"Records         : {len(attendance):,}")
print(f"Output File     : {OUTPUT_FILE}")
print("=" * 70)

print("\nAttendance Status Summary")
print("-" * 70)
print(attendance["status"].value_counts())
print("=" * 70)