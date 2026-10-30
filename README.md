
# 📚 SelfBook AI - WSP Large Project

**Developer:** Lijin T. (Lijin-1)  
**Technology Stack:** Python, FastAPI, Sentence Transformers

SelfBook AI is an AI-powered semantic search project designed to help users discover relevant nonfiction learning topics based on the meaning of their search queries.

Unlike basic keyword search, it uses sentence embeddings to identify semantically related topics.

## 1. Project Features

- AI-powered semantic search
- Natural-language search queries
- Similarity-based topic ranking
- FastAPI backend
- Interactive Swagger API documentation
- Health-check endpoint

## 2. Live Demo (When Server Is Running)

- Home: http://127.0.0.1:8000/
- API Documentation: http://127.0.0.1:8000/docs
- Health Check: http://127.0.0.1:8000/health
- Semantic Search: http://127.0.0.1:8000/search?q=I%20want%20to%20become%20wealthy

**Note:** These are local development URLs. They work only while the server is running on your computer.

## 3. How to Run

### Step 1: Install Python dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Start the FastAPI server

```bash
python -m uvicorn backend:app --reload --port 8000
```

If necessary, use:

```bash
py -m uvicorn backend:app --reload --port 8000
```

### Step 3: Open API documentation

http://127.0.0.1:8000/docs

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend API framework |
| Sentence Transformers | Text embedding generation |
| all-MiniLM-L6-v2 | Semantic embedding model |
| PyTorch | Tensor operations |
| Uvicorn | API development server |

## 5. Current Nonfiction Topics

The prototype currently includes:

- Personal Finance
- Psychology
- Self-Improvement
- Business
- Science
- History
- Technology
- Health

## 6. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Project information |
| GET | `/health` | Server health check |
| GET | `/search?q=...` | Semantic search |
| GET | `/docs` | Interactive API documentation |

### Example Search

```text
/search?q=I want to become wealthy
```

The API returns the three closest topic descriptions with similarity scores.

## 7. How Semantic Search Works

1. The user enters a natural-language query.
2. Sentence Transformer converts the query into an embedding.
3. The system compares it with stored topic embeddings.
4. Semantic similarity ranks the topics.
5. The API returns the top three results.

## 8. Current Development Status

**Version:** 0.1.0  
**Status:** Semantic Search Prototype

Currently, the system searches sample nonfiction topic descriptions. It does not yet search a complete database of real books.

### Planned Improvements

- Real nonfiction book database
- Book titles and author information
- Book descriptions and recommendations
- Improved semantic ranking
- User-friendly frontend

## 9. Important Note for Professor

GitHub stores the source code; it does not automatically run the local Python server.

To demonstrate the project:

1. Open the project folder.
2. Install the required dependencies.
3. Run the FastAPI server.
4. Open http://127.0.0.1:8000/docs.
5. Demonstrate the semantic search endpoint.

## 10. GitHub Repository

https://github.com/Lijin-1/selfbook-ai-wsp-large-project

---

**SelfBook AI — Discover knowledge through meaning.**
