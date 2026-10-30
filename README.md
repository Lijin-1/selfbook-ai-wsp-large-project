# SelfBook AI — Nonfiction Book Discovery

**Developer:** Lijin T.  
**Technology:** Python, FastAPI, Sentence Transformers  
**Project:** WSP Large Project

## Overview

SelfBook AI is a prototype nonfiction discovery API. It uses semantic search to match a user's learning goal with relevant nonfiction topics.

## Features

- FastAPI backend
- AI-powered semantic search
- Similarity scores for matching topics
- Health-check endpoint
- Interactive API documentation

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m uvicorn backend:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Project information |
| GET | `/health` | Health check |
| GET | `/search?q=book` | Original demonstration search |
| GET | `/ai-search?q=learn%20Python` | AI semantic search |
| GET | `/docs` | Interactive API documentation |

## How AI Search Works

1. The user enters a learning goal.
2. Sentence Transformers converts the query into an embedding.
3. The system compares it with sample nonfiction topic embeddings.
4. It returns the three most similar topics with similarity scores.

**Model:** `all-MiniLM-L6-v2`

## Current Limitations

- The project currently searches eight sample topic descriptions, not a real book catalogue.
- The `/search` endpoint is a demonstration endpoint with fixed scores.
- A real book database and book recommendations are future improvements.

## GitHub Repository

https://github.com/Lijin-1/selfbook-ai-wsp-large-project
