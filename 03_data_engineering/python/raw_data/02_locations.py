"""
============================================================
HR WORKFORCE ANALYTICS
Generate Office Locations Master Data
============================================================
"""

import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Output Path
# --------------------------------------------------
OUTPUT_DIR = Path("../03_data_engineering/raw_data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "02_locations.csv"

# --------------------------------------------------
# Office Location Master Data
# --------------------------------------------------
locations = [
    ("LOC001", "Global Headquarters",      "Bengaluru",   "Karnataka",      "India", "South", "Asia/Kolkata", "Headquarters"),
    ("LOC002", "Regional Office",          "Mumbai",      "Maharashtra",    "India", "West",  "Asia/Kolkata", "Regional Office"),
    ("LOC003", "Technology Center",        "Hyderabad",   "Telangana",      "India", "South", "Asia/Kolkata", "Development Center"),
    ("LOC004", "Corporate Office",         "New Delhi",   "Delhi",          "India", "North", "Asia/Kolkata", "Corporate Office"),
    ("LOC005", "Branch Office",            "Pune",        "Maharashtra",    "India", "West",  "Asia/Kolkata", "Branch Office"),
    ("LOC006", "Branch Office",            "Chennai",     "Tamil Nadu",     "India", "South", "Asia/Kolkata", "Branch Office"),
    ("LOC007", "Branch Office",            "Kolkata",     "West Bengal",    "India", "East",  "Asia/Kolkata", "Branch Office"),
    ("LOC008", "Branch Office",            "Ahmedabad",   "Gujarat",        "India", "West",  "Asia/Kolkata", "Branch Office"),
    ("LOC009", "Branch Office",            "Jaipur",      "Rajasthan",      "India", "North", "Asia/Kolkata", "Branch Office"),
    ("LOC010", "Branch Office",            "Lucknow",     "Uttar Pradesh",  "India", "North", "Asia/Kolkata", "Branch Office"),
    ("LOC011", "Regional Office",          "Kochi",       "Kerala",         "India", "South", "Asia/Kolkata", "Regional Office"),
    ("LOC012", "Technology Center",        "Noida",       "Uttar Pradesh",  "India", "North", "Asia/Kolkata", "Development Center"),
    ("LOC013", "Branch Office",            "Chandigarh",  "Chandigarh",     "India", "North", "Asia/Kolkata", "Branch Office"),
    ("LOC014", "Branch Office",            "Indore",      "Madhya Pradesh", "India", "Central","Asia/Kolkata","Branch Office"),
    ("LOC015", "Branch Office",            "Bhubaneswar", "Odisha",         "India", "East",  "Asia/Kolkata", "Branch Office")
]

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------
df = pd.DataFrame(
    locations,
    columns=[
        "location_code",
        "office_name",
        "city",
        "state",
        "country",
        "region",
        "timezone",
        "office_type"
    ]
)

# Primary Key
df.insert(0, "location_id", range(1, len(df) + 1))

# Additional Columns
df["status"] = "Active"
df["created_date"] = "2018-01-01"

# --------------------------------------------------
# Save CSV
# --------------------------------------------------
df.to_csv(OUTPUT_FILE, index=False)

print("=" * 60)
print("Locations dataset created successfully!")
print(f"Records : {len(df)}")
print(f"Saved to : {OUTPUT_FILE}")
print("=" * 60)