# ==================================================
# Configuration
# ==================================================
import random
import numpy as np
import pandas as pd

from faker import Faker
from pathlib import Path
from datetime import datetime, timedelta
TOTAL_RECRUITMENT = 3000 


from pathlib import Path

# ==============================================================
# Project Paths
# ==============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = BASE_DIR / "03_data_engineering" / "raw_data"

# Create folder if it doesn't exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RAW_DATA_DIR / "05_recruitment.csv"


recruitment_records = []

for recruitment_id in range(1, TOTAL_RECRUITMENT + 1):

    candidate_id = f"CAND{recruitment_id:06d}"

    # Generate candidate details
    # Generate department
    # Generate job role
    # Generate interview scores
    # Generate salary
    # Generate offer status
    # Generate joining status

    recruitment_records.append({
        "recruitment_id": recruitment_id,
        # remaining columns...
    })

    df = pd.DataFrame(recruitment_records)

print(f"Total Records : {len(df):,}")

df.to_csv(
    OUTPUT_FILE,
    index=False
)