from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
import os

# Load dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "employees.json")
with open(DATA_PATH, "r") as f:
    employees = json.load(f)["employees"]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------------------
# Build employee embeddings
# ---------------------------
def build_index():
    texts = []
    for emp in employees:
        profile_text = f"{emp['name']} - Skills: {', '.join(emp['skills'])}. Experience: {emp['experience_years']} years. Projects: {', '.join(emp['projects'])}. Availability: {emp['availability']}"
        texts.append(profile_text)

    embeddings = model.encode(texts)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    return index, texts

index, texts = build_index()

# ---------------------------
# Search employees by query
# ---------------------------
def search_employees_by_query(query: str, top_k: int = 3):
    query_emb = model.encode([query])
    D, I = index.search(np.array(query_emb).astype("float32"), top_k)

    results = []
    for idx in I[0]:
        emp = employees[idx]
        results.append(emp)

    return results
