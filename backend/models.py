from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class QuestionType(str, Enum):
    CODING = "coding"
    SYSTEM_DESIGN = "system_design"
    BEHAVIORAL = "behavioral"
    ML_THEORY = "ml_theory"

class Company(str, Enum):
    GOOGLE = "google"
    META = "meta"
    AMAZON = "amazon"
    MICROSOFT = "microsoft"
    APPLE = "apple"

class InterviewQuestion(BaseModel):
    question: str
    question_type: QuestionType
    company: Company
    difficulty: Optional[str] = "medium"

class Solution(BaseModel):
    approach: str
    code: Optional[str]
    complexity: dict
    explanation: str
    follow_ups: List[str]
    similar_problems: List[dict]