"""
============================================================
HR WORKFORCE ANALYTICS
Generate Job Roles Master Data
============================================================
"""

import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Output Path
# --------------------------------------------------
OUTPUT_DIR = Path("../03_data_engineering/raw_data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "03_job_roles.csv"

# --------------------------------------------------
# Job Roles
# --------------------------------------------------
job_roles = [

# Human Resources
("JR001","HR Intern","Human Resources","Intern",250000,400000),
("JR002","HR Executive","Human Resources","Junior",400000,650000),
("JR003","HR Business Partner","Human Resources","Mid",800000,1400000),
("JR004","HR Manager","Human Resources","Manager",1500000,2500000),
("JR005","HR Director","Human Resources","Director",3500000,6000000),

# Finance
("JR006","Finance Analyst","Finance","Junior",500000,800000),
("JR007","Senior Finance Analyst","Finance","Senior",900000,1500000),
("JR008","Finance Manager","Finance","Manager",1800000,3000000),
("JR009","Financial Controller","Finance","Director",3500000,6000000),

# Information Technology
("JR010","Software Engineer","Information Technology","Junior",600000,1200000),
("JR011","Senior Software Engineer","Information Technology","Senior",1200000,2200000),
("JR012","Technical Lead","Information Technology","Lead",2200000,3200000),
("JR013","Engineering Manager","Information Technology","Manager",3000000,5000000),
("JR014","Solutions Architect","Information Technology","Lead",3500000,5500000),

# Data Analytics
("JR015","Data Analyst","Data Analytics","Junior",600000,1000000),
("JR016","Business Analyst","Data Analytics","Mid",800000,1400000),
("JR017","Senior Data Analyst","Data Analytics","Senior",1200000,2000000),
("JR018","Data Scientist","Data Analytics","Senior",1800000,3000000),
("JR019","BI Developer","Data Analytics","Mid",900000,1700000),
("JR020","Analytics Manager","Data Analytics","Manager",2500000,4500000),

# Sales
("JR021","Sales Executive","Sales","Junior",400000,700000),
("JR022","Sales Consultant","Sales","Mid",600000,1100000),
("JR023","Area Sales Manager","Sales","Manager",1800000,3200000),
("JR024","Regional Sales Manager","Sales","Manager",3000000,5000000),

# Marketing
("JR025","Marketing Executive","Marketing","Junior",450000,700000),
("JR026","Digital Marketing Specialist","Marketing","Mid",700000,1200000),
("JR027","Marketing Manager","Marketing","Manager",1800000,3200000),

# Operations
("JR028","Operations Executive","Operations","Junior",450000,750000),
("JR029","Operations Manager","Operations","Manager",1800000,3200000),
("JR030","Operations Director","Operations","Director",4000000,6500000),

# Customer Support
("JR031","Customer Support Executive","Customer Support","Junior",350000,600000),
("JR032","Support Team Lead","Customer Support","Lead",800000,1400000),
("JR033","Customer Success Manager","Customer Support","Manager",1800000,3000000),

# Procurement
("JR034","Procurement Executive","Procurement","Junior",500000,800000),
("JR035","Procurement Manager","Procurement","Manager",1800000,3000000),

# Supply Chain
("JR036","Supply Chain Analyst","Supply Chain","Mid",700000,1200000),
("JR037","Logistics Manager","Supply Chain","Manager",2000000,3500000),

# Legal
("JR038","Legal Associate","Legal","Junior",700000,1200000),
("JR039","Legal Counsel","Legal","Senior",1800000,3200000),

# Administration
("JR040","Administrative Executive","Administration","Junior",350000,600000),
("JR041","Administration Manager","Administration","Manager",1200000,2200000),

# Quality Assurance
("JR042","QA Engineer","Quality Assurance","Junior",600000,1100000),
("JR043","Senior QA Engineer","Quality Assurance","Senior",1200000,2000000),

# Information Security
("JR044","Security Analyst","Information Security","Mid",900000,1600000),
("JR045","Cyber Security Manager","Information Security","Manager",2500000,4200000),

# Learning & Development
("JR046","Training Coordinator","Learning & Development","Junior",500000,800000),
("JR047","Learning Manager","Learning & Development","Manager",1800000,3000000),

# Compliance
("JR048","Compliance Officer","Compliance","Mid",900000,1500000),
("JR049","Compliance Manager","Compliance","Manager",2200000,3800000),

# Executive
("JR050","Chief Executive Officer","Executive","Executive",12000000,25000000)
]

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------
df = pd.DataFrame(job_roles, columns=[
    "job_role_code",
    "job_title",
    "department_name",
    "job_level",
    "min_salary",
    "max_salary"
])

df.insert(0, "job_role_id", range(1, len(df)+1))

df["status"] = "Active"

# --------------------------------------------------
# Save CSV
# --------------------------------------------------
df.to_csv(OUTPUT_FILE, index=False)

print("="*60)
print("Job Roles Dataset Generated Successfully")
print(f"Total Roles : {len(df)}")
print(f"Saved To    : {OUTPUT_FILE}")
print("="*60)