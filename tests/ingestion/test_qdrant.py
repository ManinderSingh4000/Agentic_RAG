from app.vectorstore.qdrant_client import QdrantManager
# from app.vectorstore.collections import create_collection

manager = QdrantManager()

manager.create_collection(
    "knowledge_base"
)

print("Collection Created")