from fastapi import FastAPI
from pydantic import BaseModel

from src.llm.analyzer import BugAnalyzer

app = FastAPI(title="AI Bug Analyzer")

analyzer = BugAnalyzer()


class ErrorRequest(BaseModel):
    error_log: str


@app.get("/")
def root():
    return {"message": "AI Bug Analyzer is running"}


@app.post("/analyze")
def analyze_error(request: ErrorRequest):

    result = analyzer.analyze(request.error_log)

    return {
        "error": request.error_log,
        "analysis": result
    }