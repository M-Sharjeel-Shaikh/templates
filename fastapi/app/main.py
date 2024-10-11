from email_validator import EmailNotValidError
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.v1.routes.crm import crmapi
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# # Include Route Here
app.include_router(crmapi)

app.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, "static"))), name="static")

# # Set up the TEMPLATES directory
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

# Example static files directory for CSS/JS if needed

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
    

# @app.get("/validateemail")
# def validate_email_quality(request: Request):
#     email = Request.get("email")

#     # Step 1: Validate email syntax
#     try:
#         v = validate_email(email)
#         email = v["email"]
#         domain = email.split('@')[-1]
#     except EmailNotValidError as e:
#         raise HTTPException(status_code=400, detail=f"Invalid email: {e}")

#     # Step 2: Check if the email domain is from a disposable email provider
#     if is_disposable_email(domain):
#         return {"email": email, "quality": "poor", "reason": "Disposable email"}

#     # Step 3: Check if the email domain has valid MX records
#     if not validate_mx_record(domain):
#         return {"email": email, "quality": "poor", "reason": "Invalid domain (no MX records)"}

#     # Step 4: (Optional) Check against third-party API for temporary email detection (e.g. use a third-party service)
#     # Here's an example of how to use a third-party API to detect temporary email services
#     # response = requests.get(f"https://api.temp-mail.org/check/{email}")
#     # if response.json().get("is_temp"):
#     #     return {"email": email, "quality": "poor", "reason": "Temporary email"}

#     # If all checks pass, mark email quality as good
#     return {"email": "email", "quality": "good", "reason": "Valid email", "request": request}

# # from faker import Faker
# from pymongo import MongoClient
# import random
# from bson.objectid import ObjectId
# from datetime import datetime, timedelta

# # Initialize Faker and MongoClient
# fake = Faker()
# client = MongoClient('mongodb://localhost:27017/')  # Adjust MongoDB URI as needed
# db = client['crm']  # Use your database name
# collection = db['leads']  # Use your collection name

# def generate_record():
#     return {
#         "_id": ObjectId(),
#         "Active": True,
#         "Company": fake.company(),
#         "Currency": "USD",
#         "Email": fake.company_email(),
#         "Expected Revenue": random.randint(5000, 20000),
#         "Opportunity": fake.catch_phrase(),
#         "Salesperson": fake.name(),
#         "Stage": random.choice(["Proposition", "Negotiation", "Closed"]),
#         "User Company": "My Company (San Francisco)",
#         "# Page Views": random.randint(0, 10),
#         "# Registrations": random.randint(0, 5),
#         "# Sessions": random.randint(0, 10),
#         "Activities": random.choice(["Send Catalog by Email", "Follow-up Call", "Meeting"]),
#         "Activity State": "Today",
#         "Activity Type Icon": "fa-envelope",
#         "Allow manual enrich": True,
#         "Assignment Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "Attachment Count": random.randint(0, 5),
#         "Automated Probability": random.randint(0, 100),
#         "Bounce": random.randint(0, 5),
#         "Campaign": random.choice(["Email Campaign - Products", "Website Campaign"]),
#         "City": fake.city(),
#         "Color Index": random.randint(0, 5),
#         "Company Name": fake.company(),
#         "Country": fake.country(),
#         "Created by": "OdooBot",
#         "Created on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "Customer": fake.company(),
#         "Days to Assign": random.randint(1, 10),
#         "Days to Close": random.randint(0, 20),
#         "Days To Convert": random.randint(0, 30),
#         "Display Name": fake.catch_phrase(),
#         "Email Domain Criterion": fake.domain_name(),
#         "Email Quality": random.choice(["Correct", "Invalid"]),
#         "Exceeded Closing Days": random.randint(0, 10),
#         "External ID": f"crm.crm_case_{random.randint(1, 100)}",
#         "Followers": f"{fake.company()}, {fake.name()}",
#         "Followers (Partners)": f"{fake.company()}, {fake.name()}",
#         "Geo Latitude": random.uniform(-90.0, 90.0),
#         "Geo Longitude": random.uniform(-180.0, 180.0),
#         "IAP Credits": random.randint(0, 100),
#         "Has Message": True,
#         "ID": random.randint(1, 100),
#         "Is Partner Visible": True,
#         "Is Won": random.choice(["Pending", "Won", "Lost"]),
#         "Kanban State": "Next activity is planned",
#         "Lang Active Count": random.randint(1, 5),
#         "Language": random.choice(["English (US)", "French", "Spanish"]),
#         "Last Stage Update": (datetime.now() - timedelta(days=random.randint(0, 5))).strftime("%Y-%m-%d %H:%M:%S"),
#         "Last Updated by": "OdooBot",
#         "Last Updated on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "Locale Code": random.choice(["en_US", "fr_FR", "es_ES"]),
#         "Medium": random.choice(["Website", "Email"]),
#         "Meeting Display Label": "No Meeting",
#         "Messages": fake.catch_phrase(),
#         "Next Activity Deadline": (datetime.now() + timedelta(days=random.randint(0, 5))).isoformat(),
#         "Next Activity Summary": random.choice(["Send Catalog by Email", "Call Client"]),
#         "Next Activity Type": "Email",
#         "Normalized Email": fake.company_email(),
#         "Number of Actions": random.randint(0, 10),
#         "Number of errors": random.randint(0, 5),
#         "Number of Quotations": random.randint(0, 5),
#         "Number of Rental Orders": random.randint(0, 5),
#         "Number of Sale Orders": random.randint(0, 5),
#         "Number of Rental Quotations": random.randint(0, 5),
#         "Phone": fake.phone_number(),
#         "Phone Quality": "Correct",
#         "Potential Duplicate Lead": "Interest in your products",
#         "Potential Duplicate Lead Count": random.randint(0, 10),
#         "Priority": random.choice(["High", "Low", "Medium"]),
#         "Probability": random.randint(0, 100),
#         "Prorated Revenue": random.uniform(1000, 10000),
#         "Responsible User": fake.name(),
#         "Sales Team": "Pre-Sales",
#         "Sanitized Number": fake.phone_number(),
#         "Source": random.choice(["Search engine", "Referral", "Email"]),
#         "Status time": {"3": random.randint(1000, 1000000)},
#         "Street": fake.street_address(),
#         "Tags": random.choice(["Software", "Hardware", "Consulting"]),
#         "Type": "Opportunity",
#         "Website": fake.url(),
#         "Zip": fake.zipcode()
#     }

# # Insert 50 records
# for _ in range(50):
#     db['leads'].insert_one(generate_record())

# print("50 documents inserted successfully.")
