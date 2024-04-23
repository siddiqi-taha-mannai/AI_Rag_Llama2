import llm_check
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

llm_check.check_and_pull_nomic_embed_text()
llm_check.check_and_pull_llama2()
    
# Embedding documents with Ollama using Nomic-embed-text
embedding=OllamaEmbeddings(model='nomic-embed-text')
db3 = Chroma(persist_directory="./VectorStore_Wiki", embedding_function=embedding)