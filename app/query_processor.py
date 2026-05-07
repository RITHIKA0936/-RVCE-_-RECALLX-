from app.memory_store import MemoryStore
from app.response_generator import ResponseGenerator


class QueryProcessor:

    def __init__(self):

        self.memory_store = MemoryStore()

    def process_query(self, query):

        # Step 1: Semantic Search
        results = self.memory_store.search_similar(query)

        # Step 2: Generate Final Response
        response = ResponseGenerator.generate(
            query,
            results
        )

        # Step 3: Return Unified Output
        return {
            "query": query,
            "response": response,
            "results": results
        }