import faiss
import numpy as np
from src.rag.embedder import get_embedding


class VectorStore:

    def __init__(self):

        self.dimension = 1536

        self.index = faiss.IndexFlatL2(self.dimension)

        self.texts = []


    def add(self, text):

        embedding = get_embedding(text)

        vector = np.array([embedding]).astype("float32")

        self.index.add(vector)

        self.texts.append(text)


    def search(self, query, k=1):

        query_embedding = get_embedding(query)

        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_vector, k)

        results = []

        for idx in indices[0]:
            results.append(self.texts[idx])

        return results


if __name__ == "__main__":

    store = VectorStore()

    store.add("TimeoutException: submit button not found")

    store.add("DatabaseConnectionError: DB unreachable")

    store.add("AssertionError: expected 200 got 500")

    query = "Submit button missing"

    result = store.search(query)

    print("Query:", query)

    print("Most similar log:", result[0])