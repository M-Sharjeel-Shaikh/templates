from fastapi import APIRouter, Depends
from app.api.v1.routes.auth import get_current_user

profile = APIRouter()

@profile.get("/profile")
async def get_user_profile(user = Depends(get_current_user)):
    return {"username": user["username"], "email": user["email"]}
