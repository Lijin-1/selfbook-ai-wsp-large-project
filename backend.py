
from fastapi import FastAPI, Query
from sentence_transformers import SentenceTransformer, util

app = FastAPI(
    title="SelfBook AI",
    version="2.0",
    description="Nonfiction Book Discovery API"
)

# Sample nonfiction topics for AI search
books = [
    "Personal finance - saving money, budgeting, investing, and wealth",
    "Psychology - understanding human behavior, emotions, and thinking",
    "Self improvement - discipline, habits, productivity, and motivation",
    "Business - entrepreneurship, management, and business strategy",
    "Science - physics, biology, chemistry, and scientific discoveries",
    "History - historical events, civilizations, and world history",
    "Technology - Python programming, coding, and artificial intelligence",
    "Health - fitness, nutrition, sleep, and healthy living",
]

# Load model and create topic embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
book_embeddings = model.encode(
    books,
    convert_to_tensor=True
)


@app.get("/")
def home():
    return {
        "project": "SelfBook AI",
        "status": "LIVE",
        "student": "Lijin.T",
        "wsp": "Large Project"
    }


@app.get("/health")
def health():
    return {"ok": True}


# Original search - preserved
@app.get("/search")
def search(q: str = ""):
    score = 0.79 if q else 0.0
    results = []

    if q:
        results = [
            {"book": f"Result for '{q}'", "relevance": score},
            {"book": "SelfBook AI Guide", "relevance": 0.85}
        ]

    return {
        "query": q,
        "score": score,
        "results": results,
        "status": "success"
    }


# New AI semantic search
@app.get("/ai-search")
def ai_search(q: str = Query(..., min_length=1)):
    query = q.strip()

    if not query:
        return {"error": "Please enter a learning goal."}

    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    results = util.semantic_search(
        query_embedding,
        book_embeddings,
        top_k=3
    )[0]

    matches = []

    for result in results:
        index = result["corpus_id"]

        matches.append({
            "book_topic": books[index],
            "similarity_score": round(result["score"], 3)
        })

    return {
        "query": query,
        "search_type": "AI semantic search",
        "results": matches
    }
