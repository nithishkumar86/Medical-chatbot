import sys
from app.common.Logs import get_logger
from app.common.configloader import load_config
from app.core.embedding_loader import LoadEmbedding
from langchain_pinecone import PineconeVectorStore
from app.common.Exceptions import MedicalBotException

logger = get_logger(__name__)

class DataRetrieval:
    def __init__(self):
        self.config = load_config()
        self.embedding = LoadEmbedding().load_embedding()

    def data_retrieval(self):
        # Implement data retrieval logic here
        vector_store = PineconeVectorStore.from_existing_index(
            index_name=self.config["collection"]["collection_name"],
            embedding=self.embedding
        )
        logger.info("Vector store is ready to convert into retrievers")
        return vector_store

    def create_retriever_as_vectorstore(self):
        try:
            vector_store = self.data_retrieval()
            retriever = vector_store.as_retriever(search_kwargs={'k': 1})
            logger.info("Retriever created successfully.")
            return retriever
        except Exception as e:
            logger.error(f"Error creating retriever: {e}")
            raise MedicalBotException(e, sys)
    
