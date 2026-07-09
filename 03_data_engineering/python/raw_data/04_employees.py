import csv
import random
from datetime import datetime, timedelta

# Configuration
OUTPUT_FILE = "employees_india.csv"
TOTAL_ROWS = 10000

# Indian Name Pools (Diverse across regions)
FIRST_NAMES_M = ["Aarav", "Arjun", "Aditya", "Rahul", "Amit", "Vijay", "Sai", "Rajesh", "Anand", "Rohan", "Vikram", "Sanjay", "Pranav", "Deepak", "Kiran"]
FIRST_NAMES_F = ["Ananya", "Diya", "Priya", "Neha", "Deepika", "Lakshmi", "Aishwarya", "Kriti", "Sneha", "Anjali", "Pooja", "Meera", "Swati", "Divya"]
LAST_NAMES = ["Sharma", "Verma", "Kumar", "Singh", "Patel", "Joshi", "Reddy", "Nair", "Iyer", "Das", "Banerjee", "Gupta", "Rao", "Choudhury", "Mehta", "Mishra"]

# Structural IDs
DEPARTMENT_IDS = [f"DEPT_{i:02d}" for i in range(1, 9)]       
JOB_ROLE_IDS = [f"ROLE_{i:03d}" for i in range(1, 25)]        

# Major Indian Tech/Business Hubs with corresponding State Location IDs
LOCATION_MAPPING = [
    {"loc_id": "LOC_BLR", "city": "Bengaluru", "state": "Karnataka"},
    {"loc_id": "LOC_HYD", "city": "Hyderabad", "state": "Telangana"},
    {"loc_id": "LOC_MUM", "city": "Mumbai", "state": "Maharashtra"},
    {"loc_id": "LOC_NCR", "city": "Gurugram/Delhi NCR", "state": "Haryana"},
    {"loc_id": "LOC_CHN", "city": "Chennai", "state": "Tamil Nadu"},
    {"loc_id": "LOC_PNQ", "city": "Pune", "state": "Maharashtra"}
]

GENDERS = ["Male", "Female", "Non-binary"]
EMPLOYMENT_TYPES = ["Full-Time", "Contract", "Intern"]
EMPLOYMENT_STATUSES = ["Active", "Active", "Active", "Active", "Resigned", "Terminated"] 
WORK_MODES = ["Onsite", "Hybrid", "Remote"]

def generate_random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randrange(days_between)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def create_indian_employee_csv(filename, total_rows):
    print(f"Generating {total_rows} realistic Indian employee records...")
    
    # Updated headers to include City and State for localized analytics
    headers = [
        "employee_id", "first_name", "last_name", "gender", "date_of_birth", 
        "email", "phone_number", "hire_date", "department_id", "job_role_id", 
        "location_id", "city", "state", "employment_type", "employment_status", 
        "salary_inr", "performance_rating", "manager_id", "work_mode", "experience_years"
    ]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for i in range(1, total_rows + 1):
            emp_id = f"EMP{i:05d}"
            
            # Gender & Name alignment
            gender = random.choices(GENDERS, weights=[52, 46, 2], k=1)[0]
            if gender == "Male":
                first_name = random.choice(FIRST_NAMES_M)
            elif gender == "Female":
                first_name = random.choice(FIRST_NAMES_F)
            else:
                first_name = random.choice(FIRST_NAMES_M + FIRST_NAMES_F)
            last_name = random.choice(LAST_NAMES)
            
            date_of_birth = generate_random_date(1965, 2004)
            email = f"{first_name.lower()}.{last_name.lower()}{i}@company.co.in"
            
            # Realistic Indian Mobile Format: +91 followed by 6, 7, 8, or 9
            phone_number = f"+91-{random.choice([6, 7, 8, 9])}{random.randint(100, 999)}-{random.randint(10000, 99999)}"
            
            hire_date = generate_random_date(2016, 2026)
            dept_id = random.choice(DEPARTMENT_IDS)
            job_role_id = random.choice(JOB_ROLE_IDS)
            
            # Pull localized geography
            loc_data = random.choice(LOCATION_MAPPING)
            loc_id = loc_data["loc_id"]
            city = loc_data["city"]
            state = loc_data["state"]
            
            emp_type = random.choices(EMPLOYMENT_TYPES, weights=[85, 12, 3], k=1)[0]
            emp_status = random.choice(EMPLOYMENT_STATUSES)
            
            manager_id = f"EMP{random.randint(1, max(1, i-1)):05d}" if i > 5 else "CEO_001"
            exp_years = random.randint(0, 38)
            
            # Realistic Indian Tech/Corporate Salaries (LPA scales heavily with experience)
            # Starting around ₹4,500,000 (~4.5 LPA) base up to senior tiers
            base_salary = random.randint(400000, 800000) 
            experience_multiplier = exp_years * random.randint(120000, 200000)
            salary_inr = base_salary + experience_multiplier
            
            # Cap realistic outliers for extreme experience
            if salary_inr > 5500000:
                salary_inr = random.randint(4500000, 6500000)
                
            perf_rating = random.randint(1, 5)
            work_mode = random.choice(WORK_MODES)
            
            writer.writerow([
                emp_id, first_name, last_name, gender, date_of_birth,
                email, phone_number, hire_date, dept_id, job_role_id,
                loc_id, city, state, emp_type, emp_status,
                salary_inr, perf_rating, manager_id, work_mode, exp_years
            ])
            
    print(f"Successfully created '{filename}' with {total_rows} rows.")

if __name__ == "__main__":
    create_indian_employee_csv(OUTPUT_FILE, TOTAL_ROWS)