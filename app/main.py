import os
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import app.db

from app.routes.auth.authManagement import router as authRouter
from app.routes.user.userManagement import router as userRouter
from app.routes.listing.listingManagement import router as listingRouter
from app.routes.wishlist.wishlistManagement import router as wishlistRouter


api_app = FastAPI()

api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_app.include_router(authRouter, prefix="/auth")
api_app.include_router(userRouter)
api_app.include_router(listingRouter, prefix="/listing")
api_app.include_router(wishlistRouter, prefix="/wishlist")


@api_app.get("/")
def read_root():
    return "Server is running"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
