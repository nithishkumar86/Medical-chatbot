from langchain_groq import ChatGroq
from app.common.Logs import get_logger
from app.common.configloader import load_config

logger = get_logger(__name__)
import os
from dotenv import load_dotenv
load_dotenv()


class ModeLoader:
    def __init__(self) -> None:
        self.config = load_config()
        self._load_environment()

    def _load_environment(self):
        load_dotenv()

        GROQ_API_KEY = os.getenv("GROQ_API_KEY")

        if not GROQ_API_KEY:
            logger.error("GROQ_API_KEY is not set in the environment variables.")
            raise ValueError("GROQ_API_KEY is required but not set.")
        
        os.environ['GROQ_API_KEY'] = GROQ_API_KEY
        logger.info("GROQ_API_KEY get successfully loaded")
    
    def load_model(self):
        llm = ChatGroq(model=self.config['model']['model_name'])
        logger.info("llm get successfully loaded")
        return llm
