from fastapi import APIRouter, FastAPI, HTTPException, Request
from pydantic import BaseModel, EmailStr
from email_validator import validate_email, EmailNotValidError
import dns.resolver
import requests
# from app.helper.email_helper import is_disposable_email, validate_mx_record

crmapi = APIRouter(tags=["CRM"])

@crmapi.get("/crm/validateemail")
async def validate_email_quality(request: Request):
    return {"message": "Hello from CRM FastAPI!  123 "}
    # email = Request.get("email")

    # # Step 1: Validate email syntax
    # try:
    #     v = validate_email(email)
    #     email = v["email"]
    #     domain = email.split('@')[-1]
    # except EmailNotValidError as e:
    #     raise HTTPException(status_code=400, detail=f"Invalid email: {e}")

    # # Step 2: Check if the email domain is from a disposable email provider
    # if is_disposable_email(domain):
    #     return {"email": email, "quality": "poor", "reason": "Disposable email"}

    # # Step 3: Check if the email domain has valid MX records
    # if not validate_mx_record(domain):
    #     return {"email": email, "quality": "poor", "reason": "Invalid domain (no MX records)"}

    # # Step 4: (Optional) Check against third-party API for temporary email detection (e.g. use a third-party service)
    # # Here's an example of how to use a third-party API to detect temporary email services
    # # response = requests.get(f"https://api.temp-mail.org/check/{email}")
    # # if response.json().get("is_temp"):
    # #     return {"email": email, "quality": "poor", "reason": "Temporary email"}

    # # If all checks pass, mark email quality as good
    # return {"email": "email", "quality": "good", "reason": "Valid email", "request": request}
    