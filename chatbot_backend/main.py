from dotenv import load_dotenv, find_dotenv
import os
load_dotenv()

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from router_hospital import router as hospital_router
from router_bacteria import router as bacteria_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # http://localhost:5173
    allow_credentials=True,
    allow_methods=["*"],                          
    allow_headers=["*"],                          
)

app.include_router(hospital_router)
app.include_router(bacteria_router)