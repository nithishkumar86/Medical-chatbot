from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
from app.common.configloader import load_config
from app.common.Logs import get_logger
import os
from langchain_pinecone import PineconeVectorStore

logger = get_logger(__name__)

class LoadEmbedding:
    def __init__(self) -> None:
        self.config = load_config()
        self._load_environment()
    
    def _load_environment(self):
        load_dotenv()

        HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')

        if not HUGGINGFACE_API_KEY:
            logger.error("HUGGINGFACE_API_KEY is not set in the environment variables.")
            raise  EnvironmentError("HUGGINGFACE_API_KEY is not set in the environment variables.")
        
        logger.info("HUGGINGFACE_API_KEY is set in the environment variables.")
        os.environ['HUGGINGFACE_API_KEY'] = HUGGINGFACE_API_KEY
    
    def load_embedding(self):
        embedding = HuggingFaceEmbeddings(model_name=self.config['embedding']['model_name'])
        logger.info(f"loaded embeded model is : {self.config['embedding']['model_name']}")
        return embedding
    
if __name__ == "__main__":
    print(LoadEmbedding().load_embedding())

