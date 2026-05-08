# System Architecture

## Architecture Overview

The project follows a modular AI memory retrieval architecture where:

1. User sends memory/query request  
2. FastAPI handles API routing  
3. Query Processor manages the workflow  
4. Memory Store handles storage + embeddings  
5. Vector Search performs semantic similarity matching  
6. Response Generator creates final human-readable output  

---

# Architecture Diagram

```text
                ┌──────────────────────┐
                │      Frontend        │
                │    (HTML / UI)       │
                └──────────┬───────────┘
                           │ HTTP Request
                           ▼
                ┌──────────────────────┐
                │      FastAPI API     │
                │    app/main.py       │
                └──────────┬───────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
┌──────────────────────┐      ┌──────────────────────┐
│    Memory Routes     │      │   Query Processor    │
│ routes/memory.py     │      │ query_processor.py   │
└──────────┬───────────┘      └──────────┬───────────┘
           │                              │
           ▼                              ▼
┌──────────────────────┐      ┌──────────────────────┐
│    Memory Store      │◄────►│   Response Generator │
│  memory_store.py     │      │ response_generator.py│
└──────────┬───────────┘      └──────────────────────┘
           │
           ▼
┌──────────────────────┐
│ SentenceTransformer  │
│  Embedding Model     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Vector Search      │
│ vector_search.py     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  memory_data.json    │
│   Persistent Memory  │
└──────────────────────┘
```

---

# Technologies Used

- FastAPI
- Python
- SentenceTransformers
- Scikit-learn
- JSON Storage
- Uvicorn
- HTML/CSS

---

# Core Features

- Semantic Search
- AI Memory Retrieval
- Embedding Generation
- Persistent Storage
- Duplicate Prevention
- Vector Similarity Matching
- REST APIs

---

# Future Enhancements

- Database Integration
- Authentication
- FAISS Vector Database
- LLM Integration
- Cloud Deployment
- Chat Interface