
from app.memory.conversation_memory import (
    ConversationMemory,
)


class MemoryManager:

    def __init__(self):

        self.memory = (
            ConversationMemory()
        )

    def save_turn(
        self,
        query: str,
        answer: str,
    ):

        self.memory.add_user_message(
            query
        )

        self.memory.add_assistant_message(
            answer
        )

    def get_context(
        self,
        limit: int = 6,
    ):

        messages = (
            self.memory.get_messages()
        )

        return messages[-limit:]