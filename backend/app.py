from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from pinecone import Pinecone

app = FastAPI(title="AI Interview Assistant")

class InterviewQuestion(BaseModel):
    question: str
    question_type: str  # coding, system_design, behavioral
    company: str

@app.get("/")
def read_root():
    return {"message": "AI Interview Assistant Backend Running"} 

@app.post("/api/solve")
async def solve_question(question: InterviewQuestion):
    # Implementation here
    pass