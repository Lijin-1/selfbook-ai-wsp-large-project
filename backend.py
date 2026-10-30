
from sentence_transformers import SentenceTransformer, util
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SelfBook AI",
    description="AI-powered nonfiction topic search",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)

# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample nonfiction topics
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

# Create embeddings
book_embeddings = model.encode(
    books,
    convert_to_tensor=True
)


@app.get("/")
def home():
    return {
        "project": "SelfBook AI",
        "status": "running",
        "search_type": "semantic search",
        "category": "nonfiction"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/search")
def search(q: str = Query(..., min_length=1)):
    query = q.strip()

    if not query:
        return {"error": "Please enter what you want to learn."}

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
        "results": matches
    }
