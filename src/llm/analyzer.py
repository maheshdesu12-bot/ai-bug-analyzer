import os
from openai import OpenAI
from dotenv import load_dotenv

from src.rag.vector_store import VectorStore

load_dotenv()

client = OpenAI()


class BugAnalyzer:

    def __init__(self):

        self.vector_store = VectorStore()

        # preload known logs
        self.vector_store.add("TimeoutException: login button not found")
        self.vector_store.add("DatabaseConnectionError: DB unreachable")
        self.vector_store.add("AssertionError: expected 200 got 500")
        self.vector_store.add("ElementNotVisibleException: submit button hidden")


    def analyze(self, error_log: str):

        similar_logs = self.vector_store.search(error_log, k=1)

        context = similar_logs[0]

        prompt = f"""
You are an expert QA automation engineer.

Error Log:
{error_log}

Similar Known Error:
{context}

Explain:

1. Root cause
2. Suggested fix

Be clear and concise.
"""

        response = client.chat.completions.create(

            model="gpt-5-mini",

            messages=[
                {"role": "system", "content": "You are an expert QA engineer."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content


if __name__ == "__main__":

    analyzer = BugAnalyzer()

    error = "Submit button missing"

    result = analyzer.analyze(error)

    print("\nError:", error)

    print("\nAI Analysis:\n")

    print(result)