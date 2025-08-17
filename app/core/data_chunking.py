from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing_extensions import List
from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from app.common.Logs import get_logger

logger = get_logger(__name__)

def load_docs(chunks:int,overlap :int) -> List[Document]:
    loader= DirectoryLoader('../', glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size = chunks, chunk_overlap = overlap)
    documents = splitter.split_documents(docs)
    logger.info(f"Total number of documents loaded: {len(documents)}")
    return documents

def filter_minimal_docs(docs : List[Document]) ->List[Document]:
    documents :List[Document] = []
    for doc in docs:
        source = doc.metadata.get('source')
        documents.append(
            Document(
                page_content = doc.page_content,
                metadata = {'source':source}
            )
        )
    logger.info(f"Total number of documents after filtering: {len(documents)}")
    return documents