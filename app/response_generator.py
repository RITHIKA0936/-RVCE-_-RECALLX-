class ResponseGenerator:

    @staticmethod
    def generate(query, search_results):

        if not search_results:
            return "No relevant memories found."

        memory_texts = []

        for result in search_results:
            memory_texts.append(result["text"])

        context = ", ".join(memory_texts)

        response = (
            f"Based on stored memories, "
            f"the system found the following relevant information: "
            f"{context}."
        )

        return response