import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Patient  # Import from models.py

# File location
csv_file = "heart.csv"  # Path to your heart.csv dataset

# Step 1: Read the CSV file
df = pd.read_csv(csv_file)
print("CSV columns:", df.columns.tolist())  # Add this line to debug

# Step 2: Database setup
engine = create_engine('sqlite:///patients.db', echo=False)
Base.metadata.create_all(engine)

# Step 3: Session setup
Session = sessionmaker(bind=engine)
session = Session()

# Add this after your imports
print("Available columns:", Patient.__table__.columns.keys())

# ... existing imports ...

# Step 4: Populate the database
for index, row in df.iterrows():
    patient_data = {
        'name': f"Patient {index}",
        'age': int(row['age']),  # Ensure it's an integer
        'gender': "Unknown",
        'blood_type': "Unknown",
        'waiting_time': 0,
        'urgency_status': "Normal",
        'is_active': True
    }
    new_patient = Patient(**patient_data)
    session.add(new_patient)

# ... rest of the code ...

# Commit the session to save changes
session.commit()
print("Database successfully populated from heart.csv!")
