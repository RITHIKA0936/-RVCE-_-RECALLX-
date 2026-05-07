from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class VectorSearchEngine:

    @staticmethod
    def search(
        query_embedding,
        memories,
        query_text,
        top_k=3
    ):

        results = []

        query_vector = np.array(
            query_embedding
        ).reshape(1, -1)

        for memory in memories:

            # Skip invalid memories
            if "embedding" not in memory:
                continue

            if "text" not in memory:
                continue

            memory_vector = np.array(
                memory["embedding"]
            ).reshape(1, -1)

            similarity = cosine_similarity(
                query_vector,
                memory_vector
            )[0][0]

            # Convert safely to string
            memory_text = str(memory["text"])
            query_text_safe = str(query_text)

            # Keyword Boost
            if query_text_safe.lower() in memory_text.lower():
                similarity += 0.50

            print(f"Checking: {memory_text}")
            print(f"Similarity: {similarity}")

            # Similarity Threshold
            if similarity > 0.30:

                results.append({
                    "text": memory_text,
                    "similarity": float(similarity),
                    "timestamp": memory.get(
                        "timestamp",
                        "No timestamp"
                    )
                })

        # Sort by highest similarity
        results = sorted(
            results,
            key=lambda x: x["similarity"],
            reverse=True
        )

        # Remove duplicate texts
        unique_results = []
        seen_texts = set()

        for result in results:

            if result["text"] not in seen_texts:

                unique_results.append(result)
                seen_texts.add(result["text"])

        return unique_results[:top_k]