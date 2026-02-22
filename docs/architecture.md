# AI Bug Analyzer Architecture

User Input
   ↓
FastAPI / CLI
   ↓
Embedding Model (OpenAI)
   ↓
FAISS Vector Database
   ↓
Retrieve Similar Logs
   ↓
LLM Analysis (GPT)
   ↓
Root Cause + Suggested Fix