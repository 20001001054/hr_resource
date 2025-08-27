from fastapi import FastAPI, Query, HTTPException
from typing import Optional
import json
import os
from .utils import search_employees_by_query


# Load dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "employees.json")
with open(DATA_PATH, "r") as f:
    employees = json.load(f)["employees"]

app = FastAPI(title="HR Resource Query Chatbot API")

@app.get("/")
def root():
    return {"message": "HR Resource Query Chatbot API is running 🚀"}

@app.get("/employees/search")
def search_employees(
    skill: Optional[str] = None,
    min_experience: Optional[int] = None,
    availability: Optional[str] = None
):
    results = employees

    if skill:
        results = [emp for emp in results if skill.lower() in [s.lower() for s in emp["skills"]]]
    if min_experience is not None:
        results = [emp for emp in results if emp["experience_years"] >= min_experience]
    if availability:
        results = [emp for emp in results if emp["availability"].lower() == availability.lower()]

    if not results:
        raise HTTPException(status_code=404, detail="No matching employees found")

    return {"results": results, "count": len(results)}

@app.get("/chat")
def chat_get(message: str):
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    # 🔹 Use semantic search
    matches = search_employees_by_query(message, top_k=3)

    if not matches:
        return {"query": message, "response": "Sorry, no matching employees found."}

    # More detailed natural language response
    response = f"Based on your requirements, I found {len(matches)} strong candidates:\n\n"
    for emp in matches:
        response += (
            f"**{emp['name']}** would be a great fit. "
            f"They have {emp['experience_years']} years of experience and have worked on "
            f"projects like {', '.join(emp['projects'])}. "
            f"Their skills include {', '.join(emp['skills'])}. "
            f"They are currently *{emp['availability']}*.\n\n"
        )

    return {"query": message, "response": response.strip()}