import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


if __name__ == "__main__":
    sample = "Login button not found"

    embedding = get_embedding(sample)

    print("Embedding length:", len(embedding))

    print("First 5 numbers:", embedding[:5])