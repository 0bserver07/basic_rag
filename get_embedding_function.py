from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function():

    embeddings = OllamaEmbeddings(model="llama3")

    return embeddings
