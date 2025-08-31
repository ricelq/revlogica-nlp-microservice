# =====================================
# This file is part of the CodeDev project
# Author: Ricel Quispe
# =====================================

# revlogica-nlp-microservice/app/main.py

from fastapi import FastAPI

app = FastAPI(title="NLP Microservice API", version="0.1.0")


@app.get("/")
def read_root():
    """
    Root endpoint for the NLP Microservice.
    """
    return {"message": "NLP Microservice is running."}
