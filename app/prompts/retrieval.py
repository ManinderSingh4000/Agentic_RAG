RETRIEVAL_PROMPT = """
You are a helpful assistant.

Conversation History:

{history}

Retrieved Context:

{context}

Question:

{query}

Instructions:
- Use the retrieved context.
- Use conversation history when needed.
- If the answer is not in the context, say:
  "I do not know."

"""