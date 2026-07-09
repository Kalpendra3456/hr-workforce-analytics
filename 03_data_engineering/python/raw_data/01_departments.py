"""
============================================================
HR WORKFORCE ANALYTICS
Generate Departments Master Data
============================================================
"""

import pandas as pd
from pathlib import Path

# -----------------------------
# Output Path
# -----------------------------
OUTPUT_DIR = Path("../03_data_engineering/raw_data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "01_departments.csv"

# -----------------------------
# Department Master Data
# -----------------------------
departments = [
    ("HR001",  "Human Resources",            "Corporate",           "CC1001",  4500000),
    ("FIN001", "Finance",                   "Corporate",           "CC1002",  8500000),
    ("IT001",  "Information Technology",    "Technology",          "CC1003", 25000000),
    ("SAL001", "Sales",                     "Commercial",          "CC1004", 18000000),
    ("MKT001", "Marketing",                 "Commercial",          "CC1005", 12000000),
    ("OPS001", "Operations",                "Business Operations", "CC1006", 32000000),
    ("CS001",  "Customer Support",          "Business Operations", "CC1007",  9000000),
    ("PROC001","Procurement",               "Supply Chain",        "CC1008",  7000000),
    ("SCM001", "Supply Chain",              "Supply Chain",        "CC1009", 22000000),
    ("LEG001", "Legal",                     "Corporate",           "CC1010",  6000000),
    ("ADM001", "Administration",            "Corporate",           "CC1011",  6500000),
    ("RD001",  "Research & Development",    "Technology",          "CC1012", 28000000),
    ("PM001",  "Product Management",        "Technology",          "CC1013", 17000000),
    ("DA001",  "Data Analytics",            "Technology",          "CC1014", 11000000),
    ("BI001",  "Business Intelligence",     "Technology",          "CC1015", 10000000),
    ("QA001",  "Quality Assurance",         "Technology",          "CC1016",  9000000),
    ("ENG001", "Engineering",               "Technology",          "CC1017", 35000000),
    ("SEC001", "Information Security",      "Technology",          "CC1018",  8000000),
    ("CMP001", "Compliance",                "Corporate",           "CC1019",  7500000),
    ("LND001", "Learning & Development",    "Human Capital",       "CC1020",  5000000),
    ("FAC001", "Facilities Management",     "Corporate",           "CC1021",  6500000),
    ("STR001", "Corporate Strategy",        "Executive",           "CC1022", 14000000),
    ("INT001", "Internal Audit",            "Corporate",           "CC1023",  7000000),
    ("COM001", "Corporate Communications",  "Corporate",           "CC1024",  5500000),
    ("PMO001", "Project Management Office", "Executive",           "CC1025",  9500000),
]

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(departments, columns=[
    "department_code",
    "department_name",
    "division",
    "cost_center",
    "annual_budget"
])

# Primary Key
df.insert(0, "department_id", range(1, len(df) + 1))

# Additional Fields
df["status"] = "Active"
df["created_date"] = "2018-01-01"

# -----------------------------
# Save CSV
# -----------------------------
df.to_csv(OUTPUT_FILE, index=False)

print("=" * 60)
print("Departments dataset created successfully!")
print(f"Records : {len(df)}")
print(f"Saved to: {OUTPUT_FILE}")
print("=" * 60)