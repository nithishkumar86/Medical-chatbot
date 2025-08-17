from app.common.configloader import load_config
from app.common.Logs import get_logger
from pinecone import ServerlessSpec
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from typing import List
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from app.core.embedding_loader import LoadEmbedding

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self) -> None:
        self.config = load_config()
        self._load_environment()
        self.embedding = LoadEmbedding().load_embedding()

    def _load_environment(self):
        load_dotenv()
        PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

        if not PINECONE_API_KEY:
            logger.error("there is no PINECONE_API_KEY")  
            raise EnvironmentError("there is no PINECONE_API_KEY")
        logger.info("PINECONE_API_KEY is loaded")
        self.pc = Pinecone(api_key=PINECONE_API_KEY)
        return self.pc

    def create_index_store_data(self,index_name:str,documents:List[Document]):
        if index_name:
            self.pc.create_index(
            name = index_name,
            dimension = 384,
            metric = 'cosine',
            spec = ServerlessSpec(cloud='aws',region='us-east-1')
            )

        index = self.pc.Index(index_name)

        vector_store = PineconeVectorStore.from_documents(documents=documents,embedding=self.embedding,index_name=index_name)
        logger.info(f"vector store is stored in the location {vector_store}")
        return {"message":"vectorstore successfully stored"}
