from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.security import decode_access_token, verify_password, get_password_hash, create_access_token
from app.db.database import db
from app.db.models import User, UserInDB
from pydantic import BaseModel
from datetime import timedelta

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class Token(BaseModel):
    access_token: str
    token_type: str

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register_user(user_data: UserRegister):
    user_exists = await db["users"].find_one({"email": user_data.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user_data.password)
    new_user = UserInDB(**user_data.dict(), hashed_password=hashed_password)
    await db["users"].insert_one(new_user.dict())
    return {"msg": "User registered successfully"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db["users"].find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = await db["users"].find_one({"username": payload.get("sub")})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
