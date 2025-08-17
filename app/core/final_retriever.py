from app.core.prompts import PROMPTS
from app.core.data_retrieval import DataRetrieval
from app.common.Logs import get_logger
from langchain_core.prompts import ChatPromptTemplate
from app.common.configloader import load_config
from langchain_core.runnables import RunnablePassthrough
from app.core.data_ingestion import DataIngestion
from app.core.data_chunking import load_docs, filter_minimal_docs
from app.core.data_retrieval import DataRetrieval
from app.core.llm_loader import ModeLoader
from langchain_core.output_parsers import StrOutputParser
from app.common.Exceptions import MedicalBotException
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import sys

logger = get_logger(__name__)

class FinalRetriever:
    def __init__(self):
        self.config = load_config()
        self.data_retrieval = DataRetrieval()
        self.data_ingestion = DataIngestion()
        self.llm = ModeLoader().load_model()
        self.pc = DataIngestion()._load_environment()

    def prompt_retrieval(self):
        prompt = ChatPromptTemplate.from_messages([
            ('system', PROMPTS['prompts']),
            ('human', "Here is the question {input}")
        ])
        logger.info("Prompt template created successfully.")
        return prompt
    
    def data_pipeline(self):
        documents = None
        try:
            documents = load_docs(chunks=self.config['chunking']['chunks'], overlap=self.config['chunking']['overlap'])
            documents = filter_minimal_docs(documents)
            logger.info(f"Loaded {len(documents)} documents from the data pipeline.")
            return documents
        except Exception as e:
            logger.error(f"Error during data pipeline: {e}")
            raise MedicalBotException(e, sys)

    def retrieval_answer(self):
        try:
            if self.pc.has_index(self.config['collection']['collection_name']):
                retriever = self.data_retrieval.create_retriever_as_vectorstore()
                logger.info(f"Retriever created for index: {self.config['collection']['collection_name']} and retrieval method: vectorstore")
                return retriever
            else:
                self.data_ingestion.create_index_store_data(index_name=self.config['collection']['collection_name'],documents=self.data_pipeline())
                retriever = self.data_retrieval.create_retriever_as_vectorstore()
                logger.info(f"Using existing index: {self.config['collection']['collection_name']} for retrieval.")
                return retriever
        except Exception as e:
            logger.error(f"Error during retrieval answer: {e}")
            raise MedicalBotException(e, sys)

    def prompt_chaining(self,question:str):
        try:
            prompt = self.prompt_retrieval()
            combine_document = create_stuff_documents_chain(llm=self.llm,prompt=prompt)
            retriever = self.retrieval_answer()
            chain = create_retrieval_chain(retriever=retriever,combine_docs_chain=combine_document)
            result = chain.invoke({'input': question})
            logger.info(f"Response generated for question: {question}")
            return result
        except Exception as e:
            logger.error(f"Error during prompt chaining: {e}")
            raise MedicalBotException(e, sys)
        

# if __name__ == "__main__":
#     question = "explain about animal bite infections with treatments and symptoms "
#     retriever_instance = FinalRetriever()
#     response = retriever_instance.prompt_chaining(question=question)
#     print(response['answer'])
