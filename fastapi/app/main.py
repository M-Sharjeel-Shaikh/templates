from email_validator import EmailNotValidError
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.v1.routes.profile import profile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# # Include Route Here
app.include_router(profile)

# Example static files directory for CSS/JS if needed
app.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, "static"))), name="static")

# # Set up the TEMPLATES directory
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
    