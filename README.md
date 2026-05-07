# AI-Powered Semantic Memory Retrieval System

An AI-powered memory engine that stores textual memories, converts them into vector embeddings using Sentence Transformers, and retrieves semantically relevant information using cosine similarity search.

---

## Features

- Semantic Memory Search
- AI Embedding Generation
- Cosine Similarity Matching
- FastAPI REST APIs
- Persistent JSON Storage
- Hybrid Keyword + Semantic Retrieval
- Dynamic AI Response Generation

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| FastAPI | API Framework |
| SentenceTransformers | Embedding Generation |
| Scikit-learn | Cosine Similarity |
| NumPy | Vector Operations |
| JSON | Persistent Storage |
| Uvicorn | Server |

---

## System Architecture

```text
User Query
     ↓
FastAPI API Endpoint
     ↓
Query Processor
     ↓
Memory Store
     ↓
Sentence Transformer
(Generate Embeddings)
     ↓
Vector Search Engine
(Cosine Similarity)
     ↓
Relevant Memory Retrieval
     ↓
Response Generator
     ↓
Final AI Response
```

---

## Project Structure

```text
backend/
│
├── app/
│   ├── main.py
│   ├── memory_store.py
│   ├── vector_search.py
│   ├── response_generator.py
│   ├── query_processor.py
│   ├── memory_data.json
│
├── requirements.txt
├── run.py

frontend/
│
├── index.html
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/add-memory` | Add memory |
| GET | `/memories` | Get all memories |
| POST | `/search` | Semantic search |

---

## Example Search Request

```json
{
  "text": "When is the project due?"
}
```

---

## Example Response

```json
{
  "query": "When is the project due?",
  "response": "Based on stored memories, the system found the following relevant information: AI project submission deadline is Friday."
}
```

---

## How It Works

1. User sends a memory or query through FastAPI APIs.
2. Sentence Transformers convert text into vector embeddings.
3. Embeddings are stored in JSON format.
4. Query embeddings are compared with stored embeddings.
5. Cosine similarity identifies the most relevant memories.
6. Response Generator creates a human-readable AI response.

---

## Future Improvements

- Database Integration
- Vector Database Support
- Frontend UI
- Authentication System
- Context-Aware Conversations
- Advanced Ranking Algorithms

---

## Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

### Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcomes

This project helped in understanding:

- Natural Language Processing (NLP)
- Sentence Embeddings
- Vector Similarity Search
- Semantic Retrieval Systems
- FastAPI Backend Development
- AI-Powered Search Systems

---

## Author

Developed as part of an AI-powered semantic retrieval system project using Python and FastAPI.

---

# 🎥 Demo Video

Watch the project demo here:

[▶ Click to Watch Demo Video](https://drive.google.com/file/d/1UqYyu6cEPcBQ5JWXSmFC-VPyCnUz38a8/view?usp=sharing)
