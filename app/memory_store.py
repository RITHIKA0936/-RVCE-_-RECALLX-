from sentence_transformers import SentenceTransformer
from datetime import datetime
import json
import os

from app.vector_search import VectorSearchEngine


# Lightweight embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

MEMORY_FILE = "app/memory_data.json"


class MemoryStore:

    def __init__(self):

        if os.path.exists(MEMORY_FILE):

            with open(MEMORY_FILE, "r") as file:
                self.memories = json.load(file)

        else:
            self.memories = []

    # Generate embedding
    def generate_embedding(self, text):

        embedding = model.encode(text)

        return embedding.tolist()

    # Add memory
    def add_memory(self, text):

        # Prevent duplicate memories
        existing_texts = [
            m["text"].lower()
            for m in self.memories
        ]

        if text.lower() in existing_texts:

            return {
                "message": "Memory already exists"
            }

        embedding = self.generate_embedding(text)

        memory = {
            "text": text,
            "embedding": embedding,
            "timestamp": datetime.now().isoformat()
        }

        self.memories.append(memory)

        self.save_memories()

        return memory

    # Save memories
    def save_memories(self):

        with open(MEMORY_FILE, "w") as file:

            json.dump(
                self.memories,
                file,
                indent=4
            )

    # Get all memories
    def get_all_memories(self):

        return self.memories

    # Semantic + keyword search
    def search_similar(self, query, top_k=5):

        query_embedding = self.generate_embedding(query)

        return VectorSearchEngine.search(
            query_embedding=query_embedding,
            memories=self.memories,
            query_text=query,
            top_k=top_k
        )